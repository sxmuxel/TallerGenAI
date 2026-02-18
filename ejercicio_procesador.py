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
    system_instruction="""Eres un Editor Editorial de prestigio.
    Tu estilo es preciso, estructurado y profesional.
    Tienes experiencia en redacción ejecutiva, edición académica y comunicación técnica.
    Siempre produces textos claros, coherentes y bien organizados.
    Encargate únicamente de entregar el resultado de la tarea solicitada, evita usar extensiones o 
    presentaciones previas como 'A continuación...' ó 'Aqui tienes...'"""
)

def procesar_articulo(texto, tarea):
    if tarea == "resumir":
        prompt = f"""
        Elabora un resumen claro y estructurado del siguiente texto:

        {texto}
        """
    elif tarea == "profesionalizar":
        prompt = f"""
        Reescribe el siguiente texto para que tenga un tono formal,
        técnico y profesional, mejorando redacción y coherencia según sea
        necesario:

        {texto}
        """
    else:
        return "Tarea no válida. Usa 'resumir' o 'profesionalizar'."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=configuration,
        contents=prompt
    )

    return response.text


# Variables y resultado
texto_usuario = input("Ingresa el texto a procesar: ")
tarea_usuario = input("Ingresa la tarea (resumir/profesionalizar): ")

resultado = procesar_articulo(texto_usuario, tarea_usuario)
print("\nResultado:\n")
print(resultado)
