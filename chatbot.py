#https://pypi.org/project/pocbot/0.3.0/
from typing import Any, Dict
from openai import OpenAI
from dotenv import load_dotenv
from pocbot.ui_templates import SingleModelChatBotUITemplate
from pocbot.chain_templates import SingleModelChatBotChain
from random import randint
import datetime
import os

now         = datetime.datetime.now()
date_name   = now.strftime("%Y-%m-%d-%H-%M-%S")
print(date_name)

# LLM Simulation
class JanBOT(SingleModelChatBotChain):
    """This is a test chain model"""
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

    def invoke(self, input_dict: Dict[str, Any]) -> str:
        user_input = input_dict["input"]
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to help and care the life of the people."},
                {"role": "user", "content": {"text": user_input}}  # Asegúrate de que el mensaje del usuario esté en un diccionario con el campo "text"
            ]
        )
        print(response)
        return response.choices[0].message.content


# UI
pocbot = SingleModelChatBotUITemplate(name="JAN-GPT", chain=JanBOT())


if __name__ == "__main__":
    pocbot()