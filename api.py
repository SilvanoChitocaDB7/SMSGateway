import json
import requests

#Api endpoint
url = "https://api.useombala.ao/v1/messages"

#Mensagem
data = {
"message": "Mensagem de teste.",
"from": "924680610",
"to": "924680610",
}

#Cabeçalho da mensagem com as específicações do SMSGateway provider (Authorization, Content-Type)
headers = {"Authorization" : "Token c570185f-ac81-4da1-a03f-85e85d5c8656","Content-Type":"application/json"}
response = requests.post(url, headers=headers, json=json.dumps(data))

# Codigo da resposta do servidor (200 para sucessso)
print(response.status_code)