import requests
import json

url = "https://bhasa-api.onrender.com/nmt_tts"

payload = json.dumps({
  "sourceLang": "en",
  "targetLang": "hi",
  "text": "This is an example sentence.",
  "gender": "female"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
audio_uri = response.json()["audioBase64"]["audioUri"]
print(audio_uri)
