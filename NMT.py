import requests
import json

url = "https://bhasa-api.onrender.com/nmt"

payload = json.dumps({
  "sourceLang": "hi",
  "targetLang": "en",
  "text": "यह एक उदाहरण वाक्य है।"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

translated_text = json.loads(response.text)["translatedText"]
print(translated_text)
