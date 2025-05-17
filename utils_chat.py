import os
from huggingface_hub import InferenceApi

token = os.getenv("HF_TOKEN")
if not token:
    raise ValueError("⚠️ Variable d’environnement HF_TOKEN manquante.")

mistral = InferenceApi("mistralai/Mistral-7B-Instruct-v0.1", token=token)

def init_chat():
    return [{"role": "system", "content": "Tu es un assistant utile."}]

def ask(prompt, history):
    history.append({"role": "user", "content": prompt})
    message = "\n".join(f"{m['role']}: {m['content']}" for m in history)
    message += "\nassistant:"

    try:
        response = mistral(message, parameters={"temperature": 0.5, "max_new_tokens": 300})
        if not response:
            return "⚠️ Aucun texte généré. La réponse est vide."
        text = response.get("generated_text", response)
        answer = text.split("assistant:")[-1].strip()
    except Exception as e:
        answer = f"❌ Erreur lors de la requête à Mistral : {e}"

    history.append({"role": "assistant", "content": answer})
    return answer
