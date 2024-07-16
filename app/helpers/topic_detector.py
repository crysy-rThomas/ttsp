import os

import fireworks.client
from dotenv import load_dotenv

load_dotenv()
fireworks.client.api_key = os.getenv("FIREWORKS_API_KEY")


def topic_detector(text):
    preprompts = "Ta réponse doit être obligatoirement en français, je te donne du texte, Je souhaite que tu me donnes en une seul phrase le topic de mon texte sous du format 'Topic : Contenu du topic', par exemple : 'Topic : Connexion d'un Pad Serveur à une caisse centrale AirKitchen.'"  # noqa: E501
    res = []

    for para in text:
        completion = fireworks.client.ChatCompletion.create(
            model="accounts/fireworks/models/mixtral-8x7b-instruct",
            messages=[
                {"role": "system", "content": preprompts},
                {"role": "user", "content": para},
            ],
            stream=False,
            n=1,
            max_tokens=500,
            temperature=0.2,
            stop=[],
        )
        message = completion.choices[0].message.content
        message = message.split(":")[1].strip()
        res.append([message, para])

    return res
