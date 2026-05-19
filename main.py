"""API del Chatbot KAVAC - Archivo Principal"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import importlib
import re

from config import APP_NAME, NOT_FOUND_MESSAGE, DEFAULT_SUGGESTIONS
from knowledge.rutas.todas_rutas import ALL_ROUTES


app = FastAPI(title=APP_NAME)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Ordenar por longitud: keywords más largas (específicas) primero
ALL_ROUTES.sort(key=lambda x: len(x[0]), reverse=True)


class QueryRequest(BaseModel):
    question: str


def keyword_score(keyword: str, question: str) -> int:
    """
    Calcula qué tan bien coincide una keyword con la pregunta.
    Mayor puntaje = mejor match.
    - 100: match exacto
    - 80:  la pregunta empieza con la keyword
    - 60:  la keyword aparece como palabra completa
    - 40:  la keyword está contenida como substring
    - 0:   no coincide
    """
    q = question.lower()
    kw = keyword.lower()
    
    if q == kw:
        return 100
    if q.startswith(kw):
        return 80
    if re.search(r'\b' + re.escape(kw) + r'\b', q):
        return 60
    if kw in q:
        return 40
    return 0


def find_answer(question: str):
    """Busca la mejor respuesta usando puntaje de coincidencia"""
    q_lower = question.lower()
    
    best_keyword = None
    best_module = None
    best_func = None
    best_suggestions = []
    best_score = 0
    
    for keyword, module_name, func_name, suggestions in ALL_ROUTES:
        score = keyword_score(keyword, q_lower)
        
        if score > best_score:
            best_score = score
            best_keyword = keyword
            best_module = module_name
            best_func = func_name
            best_suggestions = suggestions
    
    if best_score >= 40:
        try:
            module = importlib.import_module(best_module)
            func = getattr(module, best_func)
            return func(), best_suggestions
        except Exception:
            pass
    
    return None, []


@app.get("/health")
async def health():
    return {"status": "OK", "routes_loaded": len(ALL_ROUTES)}


@app.post("/query")
async def query(request: QueryRequest):
    answer, suggestions = find_answer(request.question.strip())
    
    if answer:
        return {"success": True, "answer": answer, "suggestions": suggestions}
    
    return {"success": False, "answer": NOT_FOUND_MESSAGE, "suggestions": DEFAULT_SUGGESTIONS}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)