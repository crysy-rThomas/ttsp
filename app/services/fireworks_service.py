import os
import requests
import json
from dotenv import load_dotenv
from helpers.rag import rag


class FireworksService:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("FIREWORKS_API_KEY")

    def inference(self, messages):
        rag_split = rag(messages[-1]["content"])
        if rag_split != []:  # Check if rag_split is not an empty list
            # Assuming rag_split is expected to contain only one item when not empty
            preprompts = {
                "role": "system",
                "content": f"Ta réponse doit être obligatoirement en français. Voici le résultat de recherche effectué : {rag_split.content}",
            }
            print("utilisation du rag")
        else:
            # Handle the case when rag_split is empty
            # For example, set a default message or perform some other action
            preprompts = {
                "role": "system",
                "content": "Ta réponse doit être obligatoirement en français.",
            }
            print("pas de rag")
        messages = [preprompts] + messages

        url = "https://api.fireworks.ai/inference/v1/chat/completions"
        payload = {
            "model": "accounts/fireworks/models/mixtral-8x7b-instruct",
            "max_tokens": 4096,
            "top_p": 1,
            "top_k": 40,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "temperature": 0.6,
            "messages": messages,
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            raise Exception(f"Request failed: {response.status_code} - {response.text}")
        return response.json()
