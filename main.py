from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Tuple
from chromadb import PersistentClient
from chromadb.utils import embedding_functions
import logging
import re
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=500)
    top_k: int = Field(5, ge=3, le=15)

class QueryResponse(BaseModel):
    success: bool
    answer: str
    sources: List[str]
    confidence: float

# Inicializar ChromaDB
client = PersistentClient(path="./chroma_db")
ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = client.get_collection(name="mis_documentos_md", embedding_function=ef)

def identify_query_type(question: str) -> Tuple[str, str]:
    """
    Identificar el tipo de consulta y extraer la entidad principal
    Retorna: (tipo_consulta, entidad)
    """
    question_lower = question.lower()
    
    # Patrones para diferentes tipos de consultas
    patterns = [
        # (regex, tipo_consulta)
        (r'(?:qué|que)\s+(?:es|son)\s+(?:un|una|el|la|los|las)?\s*(\w+(?:\s+\w+){0,3})', 'definicion'),
        (r'(?:definición|definicion|concepto|significado)\s+(?:de|del)?\s*(\w+(?:\s+\w+){0,3})', 'definicion'),
        (r'(?:cuáles|cuales)\s+(?:son|serían)\s+(?:los|las)?\s*(\w+(?:\s+\w+){0,3})', 'lista'),
        (r'(?:cómo|como)\s+(?:funciona|trabaja|opera)\s+(?:el|la)?\s*(\w+(?:\s+\w+){0,3})', 'funcionamiento'),
        (r'(?:módulos|modulos|componentes|partes)\s+(?:de|del)?\s*(\w+(?:\s+\w+){0,3})', 'modulos'),
    ]
    
    for pattern, qtype in patterns:
        match = re.search(pattern, question_lower)
        if match:
            entity = match.group(1).strip()
            return qtype, entity
    
    # Si no coincide con ningún patrón, buscar la palabra más importante
    words = question_lower.split()
    # Filtrar palabras vacías (stopwords)
    stopwords = {'que', 'es', 'el', 'la', 'los', 'las', 'un', 'una', 'de', 'del', 'para', 'por', 'como'}
    keywords = [w for w in words if w not in stopwords and len(w) > 2]
    
    if keywords:
        return 'general', ' '.join(keywords[:2])
    
    return 'general', question

def is_definition_chunk(chunk: str, entity: str) -> bool:
    """
    Determinar si un chunk es una definición de la entidad
    """
    chunk_lower = chunk.lower()
    entity_lower = entity.lower()
    
    # La entidad debe aparecer al inicio o cerca del inicio
    if entity_lower not in chunk_lower[:200]:
        return False
    
    # Patrones que indican definición
    definition_patterns = [
        rf'{entity}\s+es\s+',
        rf'{entity}\s+son\s+',
        rf'{entity}\s+se\s+define',
        rf'{entity}\s+significa',
        rf'{entity}\s+está\s+compuesto',
        rf'{entity}\s+consiste\s+en',
        rf'{entity}\s+es\s+una\s+',
        rf'{entity}\s+es\s+un\s+',
    ]
    
    for pattern in definition_patterns:
        if re.search(pattern, chunk_lower):
            return True
    
    return False

def extract_best_sentence(chunk: str, entity: str) -> str:
    """
    Extraer la mejor oración que contiene la definición
    """
    sentences = re.split(r'(?<=[.!?])\s+', chunk)
    entity_lower = entity.lower()
    
    # Primero buscar oraciones con patrones de definición
    for sentence in sentences:
        sent_lower = sentence.lower()
        if entity_lower in sent_lower[:100]:
            if any(pattern in sent_lower for pattern in [' es ', ' son ', 'define', 'significa', 'consiste']):
                return sentence.strip()
    
    # Luego, la primera oración que contenga la entidad
    for sentence in sentences:
        if entity_lower in sentence.lower():
            return sentence.strip()
    
    # Si no, devolver el chunk completo pero truncado
    return chunk[:500] + "..." if len(chunk) > 500 else chunk

def score_chunk_relevance(chunk: str, entity: str, query_type: str) -> float:
    """
    Puntuar la relevancia de un chunk
    """
    chunk_lower = chunk.lower()
    entity_lower = entity.lower()
    
    score = 0.0
    
    # Puntos por contener la entidad
    if entity_lower in chunk_lower:
        score += 10
        # Bonus si aparece al inicio
        if entity_lower in chunk_lower[:100]:
            score += 5
    
    # Bonus según tipo de consulta
    if query_type == 'definicion':
        definition_indicators = [' es ', ' son ', 'define', 'significa', 'concepto']
        for ind in definition_indicators:
            if ind in chunk_lower:
                score += 3
    
    elif query_type == 'modulos':
        module_indicators = ['módulo', 'modulo', 'componente', 'funcionalidad']
        for ind in module_indicators:
            if ind in chunk_lower:
                score += 3
    
    # Penalizar si parece ser sobre otra cosa
    if query_type == 'definicion' and 'módulo' in chunk_lower and 'módulo' not in entity_lower:
        score -= 5
    
    return score

@app.get("/health")
async def health():
    return {"status": "OK", "chunks": collection.count()}

@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    question = request.question.strip()
    logger.info(f"📝 Pregunta: '{question}'")
    
    # Identificar tipo de consulta y entidad
    query_type, entity = identify_query_type(question)
    logger.info(f"🔍 Tipo: {query_type}, Entidad: '{entity}'")
    
    # Buscar documentos (pedir más para filtrar)
    results = collection.query(
        query_texts=[question],
        n_results=min(15, collection.count())
    )
    
    if not results['documents'][0]:
        return QueryResponse(
            success=False,
            answer="No encontré información sobre eso en la documentación.",
            sources=[],
            confidence=0.0
        )
    
    chunks = results['documents'][0]
    metadatas = results['metadatas'][0]
    distances = results['distances'][0]
    
    # Evaluar cada chunk
    scored_chunks = []
    for i, chunk in enumerate(chunks):
        score = score_chunk_relevance(chunk, entity, query_type)
        # Ajustar por distancia semántica (menor distancia = mayor similitud)
        semantic_score = 1.0 - min(distances[i], 1.0)
        final_score = score + (semantic_score * 5)
        
        scored_chunks.append({
            'chunk': chunk,
            'metadata': metadatas[i],
            'score': final_score,
            'distance': distances[i]
        })
    
    # Ordenar por puntuación
    scored_chunks.sort(key=lambda x: x['score'], reverse=True)
    
    # Seleccionar el mejor
    best = scored_chunks[0]
    
    # Extraer la mejor parte
    if query_type in ['definicion', 'modulos', 'funcionamiento']:
        answer = extract_best_sentence(best['chunk'], entity)
    else:
        # Para consultas generales, devolver el chunk completo pero limpio
        answer = best['chunk'].strip()
    
    # Calcular confianza
    confidence = (1.0 - best['distance']) * 100
    
    logger.info(f"✅ Respuesta: {answer[:100]}...")
    
    return QueryResponse(
        success=True,
        answer=answer,
        sources=[best['metadata'].get('source', 'desconocido')],
        confidence=round(confidence, 2)
    )

if __name__ == "__main__":
    import uvicorn
    logger.info("🚀 Iniciando servidor...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
