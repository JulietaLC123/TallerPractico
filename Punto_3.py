import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar variables de entorno desde el archivo .env
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente de la API de Google GenAI
client = genai.Client(api_key=API_KEY)

# Configuración del modelo para que sea un vendedor amable
configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    system_instruction="""Eres un vendedor amable.
Tus respuestas deben ser concisas, coherentes y orientadas a brindar información útil sobre productos tecnológicos.
""",
)

# Ejemplos de conversación pre-cargados (historial)
history = """
Cliente: ¿Qué características tiene el teléfono móvil Galaxy S22?
Agente: El Galaxy S22 tiene una pantalla Dynamic AMOLED 2X de 6.1 pulgadas, un procesador Exynos 2200, 8 GB de RAM y una cámara principal de 50 MP. Su batería es de 3700 mAh y es compatible con carga rápida de 25W.

Cliente: ¿Cuánto cuesta la laptop MacBook Pro 13?
Agente: La MacBook Pro de 13 pulgadas viene con el chip M2, 8 GB de RAM, y 256 GB de almacenamiento SSD. Su precio es de $1,299 USD.
"""

# Prompt para el modelo con el historial de conversación inicial
prompt = f"""En base a este historial de conversación, continúa respondiendo de forma amable y concisa a las preguntas del cliente.

{history}
"""

# Configuración adicional para la llamada
configuracion = types.GenerateContentConfig(
    temperature= 0.9,  # Controla la creatividad de la respuesta
    max_output_tokens= 400,  # Límite de tokens para la respuesta
)

# Bucle interactivo para recibir preguntas del cliente
while True:
    user_input = input("Cliente: ")
    
    if user_input.lower() in ["finalizar", "salir", "exit", "quit"]:
        print("Asistente: ¡Hasta pronto! Gracias por visitar nuestra tienda.")
        break
    
    # Agregar la entrada del usuario al historial
    prompt += f"Cliente: {user_input}\n"
    
    # Llamada directa al servicio de modelos
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",  # Especifica el modelo adecuado
            contents=prompt,
            config=configuracion
        )
    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")
        continue  # Si hay un error, sigue pidiendo más preguntas
    
    # Imprimir la respuesta del modelo
    if response:
        print(response.text)
    
    # Agregar la respuesta del asistente al historial para continuar la conversación
    prompt += f"Agente: {response.text}\n"
