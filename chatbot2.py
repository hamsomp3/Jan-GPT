from openai import OpenAI
from dotenv import load_dotenv
import datetime
import os
import streamlit as st

class JanGPT:
    def __init__(self):
        self.load_api_key()
        self.client = OpenAI(api_key=self.api_key)
    
    def load_api_key(self):
        """
        Carga la clave API de OpenAI desde un archivo .env.
        """
        load_dotenv()
        self.api_key = os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("La variable de entorno OPENAI_API_KEY no está definida")
    def chat_jan(self, user_input):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to help and care the life of the people."},
                {"role": "user", "content": user_input}  # Asegúrate de que el mensaje del usuario esté en un diccionario con el campo "text"
            ]
        )
        print(response)
        return response.choices[0].message.content
    
if __name__ == "__main__":
    jan = JanGPT()
    if user_input := st.chat_input("Aks me anything:"):
        st.write(jan.chat_jan(user_input))
    
    
    # user_input = input("You: ")
    # print(jan.chat_jan(user_input))