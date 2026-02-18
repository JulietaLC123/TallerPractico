import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv() # Load environment variables from .env file
API_KEY = os.getenv("GENAI_API_KEY")
# Inicializar el cliente
client = genai.Client(api_key=API_KEY)
configuration = types.GenerateContentConfig(
 max_output_tokens=2048,
 system_instruction="""Eres un asistente de estudio especializado en Inferencia en IA.
Tus respuestas deben ser concisas, educativas teniendo presente que el usuario es un estudiante de Ingeniería de sistemas.
Tus respuestas no deben tener mas de 50 palabras.
Si te hacen una pregunta que no está realicionada con la Inteligencia Artificial, responde 'Lo siento, solo puedo responder preguntas relacionadas con temas relacionados a la Inferencia en IA. """
)
text = input("Escribe tu pregunta sobre Inferencia en IA: ")
response = client.models.generate_content(
 model="gemini-2.5-flash",
 config=configuration,
 contents=text
)
print(response.text)
