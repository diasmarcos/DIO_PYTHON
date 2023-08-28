import json
file_json = open('dados.json')
pessoas = json.load(file_json)
print(json.dumps(pessoas,indent=2))

openai_api_key = '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'

from openai.api_resources import completion
import openai
openai.api_key = openai_api_key
def generete_ai_news(user):
  MODEL = "gpt-3.5-turbo"
  completion = openai.ChatCompletion.create(
      model=MODEL,
      messages=[
          {
              "role": "system",
              "content": "Você é um guia tiristico."
          },
          {
              "role": "user",
              "content": f"Explique para {user['nome']} o que tem de bom na cidade {user['cidade']}-{user['estado']} (máximo 100 caracteres)"
          }
      ]
  )

  responseChatGPT = completion.choices[0].message.content.strip('\"')
  return responseChatGPT


for user in pessoas:
  news = generete_ai_news(user)
  print(f"Cidade de {user['cidade']} tem {news}")
  user.update({"Info": news})

print(pessoas)
# def update_user(user):
#   response = requests.put(f"{swd2023_api_url}/users/{user['id']}",json =user)
#   return True if response.status_code==200 else False
# for user in pessoas:
#   success =update_user(user)
#   print(f"user {user['name']}, id:{user['id']} updated? {success}!")
