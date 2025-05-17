import os
from huggingface_hub import InferenceApi

token = os.getenv("HF_TOKEN")
if not token:
    raise ValueError(" Variable denvironnement HF_TOKEN manquante.")

mistral = InferenceApi("mistralai/Mistral-7B-Instruct-v0.1", token=token)

def init_chat():
    return {.git,README.md,app.py,modules,requirements.txt,utils_chat.py} "role": "system", "content": "Tu es un assistant utile.""role": "user", "content": prompt)
    message = "n".join(f"{.git,README.md,app.py,modules,requirements.txt,utils_chat.py}" mole': montent'" for m in history)
    message += "nassistant:"

    try:
        response = mistral(message)
        text = response.get("generated_text", response)
        answer = text.split("assistant:") Erreur lors de la requte  Mistral : {.git,README.md,app.py,modules,requirements.txt,utils_chat.py} e"

    history.append({.git,README.md,app.py,modules,requirements.txt,utils_chat.py} "role": "assistant", "content": answer)
    return answer
