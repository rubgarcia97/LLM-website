from openai import OpenAI

import json

path = "./api_openai.json"
with open(path) as file:
    data = json.load(file)
    api_key = data.get('OpenAIToken',None)

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Cual es la capital de Alemania?"}
    ]
)

print(response.choices[0].message.content)