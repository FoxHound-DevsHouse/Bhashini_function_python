import requests
import json

url = "https://bhasa-api.onrender.com/asr_nmt"

payload = json.dumps({
  "sourceLang": "hi",
  "targetLang": "en",
  "base64Audio": "BASE64_ENCODED_AUDIO_DATA"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
