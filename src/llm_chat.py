from openai import OpenAI

import json

class Chat:

    def __init__(self) -> None:
        pass

    def request(self,input_1,input_2, input_3,input_4):

        path = "../api_openai.json"
        with open(path) as file:
            data = json.load(file)
            api_key = data.get('OpenAIToken',None)

        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente dietista y tu mision principal es aportar recetas de comida que sean saludables"},
                {"role": "user", "content": f"Hoy me apetece para {input_1} algo que tenga {input_2}, tambien ten en cuenta lo siguiente en cuanto a kcal e ingredientes {input_3}, {input_4}"}
            ]
        )

        return response.choices[0].message.content