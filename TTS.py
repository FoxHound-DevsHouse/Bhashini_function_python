import requests
import json

url = "https://bhasa-api.onrender.com/tts"

payload = json.dumps({
  "sourceLang": "hi",
  "text": "यह एक उदाहरण वाक्य है।",
  "gender": "male"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
