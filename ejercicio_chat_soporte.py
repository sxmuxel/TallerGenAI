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
    system_instruction="""Eres un vendedor amable y profesional de una tienda de tecnología.
    Siempre respondes con cordialidad, claridad y ofreciendo especificaciones técnicas 
    relevantes de los productos. También sugieres productos similares cuando sea apropiado."""     
)

# Inicializar el chat
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=configuration,
    history=[
        {
            "role": "user",
            "parts": [{"text": "¿Qué características tiene la laptop Lenovo IdeaPad 3?"}]
        },
        {
            "role": "model",
            "parts": [{"text": "La Lenovo IdeaPad 3 cuenta con procesador Intel Core i5 de 11ª generación, 8GB de RAM, SSD de 512GB y pantalla Full HD de 15.6 pulgadas. Es ideal para estudiantes y trabajo de oficina."}]
        },
        {
            "role": "user",
            "parts": [{"text": "¿Qué me puedes decir del iPhone 14?"}]
        },
        {
            "role": "model",
            "parts": [{"text": "El iPhone 14 ofrece pantalla Super Retina XDR de 6.1 pulgadas, chip A15 Bionic, cámara dual de 12MP y almacenamiento desde 128GB. Destaca por su rendimiento y calidad fotográfica."}]
        }
    ]
)

print("--- Chat con IA para Tienda de Tecnología ---")
print("(Escribe 'finalizar' para terminar la conversación)\n")

while True:
    user_input = input("Cliente: ")

    if user_input.lower() in ["finalizar"]:
        print("Tienda: ¡Hasta Pronto! Fue un placer colaborarte.")
        break    
    try:
        response = chat.send_message(user_input)
        print(f"\nAsistente: {response.text}\n")
    except Exception as e:
        print(f"Error al procesar la solicitud: {e}")
    
