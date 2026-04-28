from google import genai
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from django.conf import settings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

client = genai.Client()

def get_embedding(texto):
    """Genera embedding usando Gemini Embedding 2"""
    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=texto
    )
    return result.embeddings[0].values

def procesar_url_rag(url, query=None, top_k=3):
    # 1. Cargar texto
    loader = WebBaseLoader(url)
    docs = loader.load()
    
    # 2. Limpiar texto
    texto_limpio = "\n".join([line.strip() for line in docs[0].page_content.splitlines() if line.strip()])
    
    MAX_CARACTERES = 15000
    if len(texto_limpio) > MAX_CARACTERES:
        texto_limpio = texto_limpio[:MAX_CARACTERES]
    
    # 3. Dividir en chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_text(texto_limpio)
    
    if not query or not chunks:
        return chunks[:top_k]
    
    # 4. Generar embedding de la consulta
    consulta_formateada = f"task: search result | query: {query}"
    query_emb = get_embedding(consulta_formateada)
    
    # 5. Generar embeddings de los chunks
    chunk_data = []
    for chunk in chunks:
        doc_formateado = f"title: none | text: {chunk}"
        chunk_emb = get_embedding(doc_formateado)
        chunk_data.append({"texto": chunk, "embedding": chunk_emb})
    
    # 6. Calcular similitud (cosine similarity)
    query_vector = np.array(query_emb).reshape(1, -1)
    chunk_vectors = np.array([item["embedding"] for item in chunk_data])
    
    similarities = cosine_similarity(query_vector, chunk_vectors)[0]
    
    # 7. Obtener los top_k más similares
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    resultados = [chunk_data[i]["texto"] for i in top_indices]
    
    return resultados


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