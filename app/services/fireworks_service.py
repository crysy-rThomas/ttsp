import os
import fireworks.client
from dotenv import load_dotenv

from helpers.rag import rag


class FireworksService:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("FIREWORKS_API_KEY")

    def inference(self, messages):

        rag_split = rag(messages[-1]["content"])
        if rag_split != []:  # Check if rag_split is not an empty list
            preprompts = {
                "role": "assistant",
                "content": f"Ma réponse doit être obligatoirement en français. Voici le résultat de recherche effectué : {rag_split.content}"
            }
            print('utilisation du rag')
        else:
            preprompts = {
                "role": "assistant",
                "content": "Ma réponse doit être obligatoirement en français."
            }
            print('pas de rag')
        messages = [preprompts] + messages

        completion = fireworks.client.ChatCompletion.create(
            model="accounts/fireworks/models/mixtral-8x7b-instruct",
            messages=messages,
            stream=False,
            n=1,
            max_tokens=4096,
            temperature=0.6,
            stop=[],
        )
        message = completion.choices[0].message.content
        return message
