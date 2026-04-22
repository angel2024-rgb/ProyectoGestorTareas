from google import genai
from dotenv import load_dotenv

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
import hashlib

load_dotenv()

client = genai.Client()

def procesar_url_rag(url, query=None, top_k=3):

    # 1. Cargar texto
    loader = WebBaseLoader(url)
    docs = loader.load()
    
    # 2. Limpiar texto
    texto_limpio = "\n".join([line.strip() for line in docs[0].page_content.splitlines() if line.strip()])
    
    # 3. Dividir en chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(texto_limpio)
    
    # 4. Generar embeddings
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)
    
    # 5. Guardar en ChromaDB
    client = chromadb.PersistentClient(path="./data/chromadb")
    
    collection_name = f"url_{hashlib.md5(url.encode()).hexdigest()[:8]}"
    
    try:
        client.delete_collection(collection_name)
    except:
        pass
    
    collection = client.create_collection(collection_name)
    
    collection.add(
        documents=chunks,
        ids=[f"c_{i}" for i in range(len(chunks))],
        embeddings=embeddings.tolist()
    )
    
    # 6. Si hay query, buscar mejores coincidencias
    if query:
        query_emb = model.encode([query]).tolist()
        results = collection.query(query_embeddings=query_emb, n_results=top_k)
        return results["documents"][0] if results["documents"] else []
    
    return None

def sugerir_subtareas(descripcion_tarea: str, url: str = None) -> str:
    # Si hay URL, buscar con contexto
    contexto = ""
    if url:
        fragmentos = procesar_url_rag(url, query=descripcion_tarea, top_k=3)
        if fragmentos:
            contexto = f"\n\nBasado en este contexto de la URL:\n{'---'.join(fragmentos)}\n\n"
    
    # Si no, solo llamar a llamar a Gemini con la descripción de la tarea
    prompt = f"{contexto}Genera una lista de subtareas para: {descripcion_tarea}"
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )
    return response.text
