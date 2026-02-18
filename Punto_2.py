import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # Cargar variables de entorno desde el archivo .env
API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente
client = genai.Client(api_key=API_KEY)
configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    system_instruction="""Eres un asistente de estudio especializado en Editor de una editorial de prestigio.
Tus respuestas deben ser concisas.
""",
)

# Inicialización del chat
chat = client.chats.create(model="gemini-2.5-flash", config=configuration)

# Función para procesar el artículo según la tarea
def procesar_articulo(texto, tarea):
    """
    Procesa un artículo según la tarea especificada.
    
    :param texto: El texto largo del artículo.
    :param tarea: La tarea a realizar (por ejemplo: 'resumir', 'profesionalizar', etc.)
    :return: Respuesta generada por el modelo de IA.
    """
    if tarea.lower() == "resumir":
        prompt = f"Resumir este artículo de manera concisa y clara en un resumen ejecutivo. El artículo es el siguiente:\n{texto}"
    elif tarea.lower() == "profesionalizar":
        prompt = f"Editar el siguiente artículo para que suene formal, técnico y adecuado para un contexto profesional. El artículo es el siguiente:\n{texto}"
    else:
        return "Tarea no reconocida. Por favor ingresa 'resumir' o 'profesionalizar'."
    
    # Enviar el mensaje al modelo
    response = chat.send_message(prompt)
    
    # Acceder a la respuesta correcta del objeto 'response'
    respuesta_ia = response.text  # Accedemos a la respuesta correctamente
    
    return respuesta_ia

# Ejemplo de uso
if __name__ == "__main__":
    print("--- Chat de Estudio IA ---")
    print("(Escribe 'salir' para terminar)\n")

    while True:
        tarea = input("Ingresa la tarea (por ejemplo, 'resumir', 'profesionalizar'): ")
        if tarea.lower() == 'salir':
            break
        articulo = input("Ingresa el texto del artículo: ")
        resultado = procesar_articulo(articulo, tarea)
        print("\nResultado de la tarea:\n")
        print(resultado)
        print("\n")
