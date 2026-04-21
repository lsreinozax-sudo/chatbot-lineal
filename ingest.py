import os
import glob
from chromadb import PersistentClient
from chromadb.utils import embedding_functions

# Configuración
DOCS_DIR = "./docs"
CHROMA_PATH = "./chroma_db"
COLLECTION = "mis_documentos_md"

# Crear cliente
client = PersistentClient(path=CHROMA_PATH)

# Modelo de embeddings
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Crear colección
collection = client.get_or_create_collection(
    name=COLLECTION,
    embedding_function=ef
)

# Procesar archivos .md
os.makedirs(DOCS_DIR, exist_ok=True)
md_files = glob.glob(f"{DOCS_DIR}/*.md")

for file_path in md_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    chunks = [c.strip() for c in content.split('\n\n') if len(c.strip()) > 20]
    
    if chunks:
        ids = [f"{os.path.basename(file_path)}_{i}" for i in range(len(chunks))]
        collection.upsert(
            ids=ids,
            documents=chunks,
            metadatas=[{"source": file_path} for _ in chunks]
        )
        print(f"✅ {file_path}: {len(chunks)} chunks")

print(f"\n📊 Total: {collection.count()} chunks en '{COLLECTION}'")
