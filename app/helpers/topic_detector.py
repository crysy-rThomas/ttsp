import os

import fireworks.client
from dotenv import load_dotenv

load_dotenv()
fireworks.client.api_key = os.getenv("FIREWORKS_API_KEY")


def topic_detector(text):
    preprompts = "I give you some text, i want you to give the topic in one sentence of this text with this format: 'Topic : Contenu du topic', for exemple : 'Topic : Connection from a phone to a PC.'"  # noqa: E501
    res = []

    for para in text:
        print(para)
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
