import requests
import json

url = "https://bhasa-api.onrender.com/asr_nmt_tts"

payload = json.dumps({
  "sourceLang": "hi",
  "targetLang": "en",
  "base64Audio": "BASE64_ENCODED_AUDIO_DATA",
  "gender": "male"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
