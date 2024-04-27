from openai import OpenAI

import json

class Chat:

    def __init__(self) -> None:
        pass

    def request(self,input_1,input_2):

        path = "./api_openai.json"
        with open(path) as file:
            data = json.load(file)
            api_key = data.get('OpenAIToken',None)

        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente dietista y tu mision principal es aportar recetas de comida que sean saludables"},
                {"role": "user", "content": f"Hoy me apetece {input_1} para {input_2}"}
            ]
        )

        return response.choices[0].message.content