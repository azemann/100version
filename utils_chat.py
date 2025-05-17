import os
import requests

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("⚠️ Variable OPENROUTER_API_KEY manquante.")

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "mistral/mistral-7b-instruct"  # Modifiable à tout moment

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def init_chat():
    return [{"role": "system", "content": "Tu es un assistant IA francophone, clair, logique et créatif."}]

def ask(prompt, history):
    history.append({"role": "user", "content": prompt})
    try:
        response = requests.post(API_URL, headers=headers, json={
            "model": MODEL,
            "messages": history,
            "temperature": 0.7
        })
        response.raise_for_status()
        answer = response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        answer = f"❌ Erreur OpenRouter : {e}"
    history.append({"role": "assistant", "content": answer})
    return answer
