import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv() 
API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente
client = genai.Client(api_key=API_KEY)

configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    system_instruction="""Eres un experto en IA técnico pero conciso. 
    Tu única tarea es explicar qué es la 'Inferencia en IA'.
    REGLA CRÍTICA: La respuesta debe tener menos de 50 palabras. 
    No uses introducciones como 'Claro' o 'Aquí tienes'. Ve al grano."""
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=configuration,
    contents="Explica que es la Inferencia en IA"
)

print(response.text)