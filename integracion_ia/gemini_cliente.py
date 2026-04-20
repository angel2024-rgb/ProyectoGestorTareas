from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

def sugerir_subtareas(descripcion_tarea: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"Divide esta tarea en subtareas claras: {descripcion_tarea}"
    )
    return response.text

def resumir_tarea(descripcion_tarea: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"Resume esta tarea en una frase: {descripcion_tarea}"
    )
    return response.text