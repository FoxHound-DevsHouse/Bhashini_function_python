import requests
import json

url = "https://bhasa-api.onrender.com/asr"
base64="<MY_BASE64_CODE>"
payload = json.dumps({
  "sourceLang": "bn",
  "base64Audio": base64
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

transcribed_text = json.loads(response.text)["text"]
print(transcribed_text)
