import os
import fireworks.client
from dotenv import load_dotenv


class FireworksService:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("FIREWORKS_API_KEY")

    def inference(self, messages):
        preprompts = {"role":"system","content":"Ta réponse doit être obligatoirement en français"}

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
