import os
from huggingface_hub import InferenceClient

token = os.getenv("HF_TOKEN")
if not token:
    raise ValueError(" Variable denvironnement HF_TOKEN manquante.")

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    token=token
)

def init_chat():
    return {.git,README.md,app.py,modules,requirements.txt,utils_chat.py} "role": "system", "content": "Tu es un assistant utile.""role": "user", "content": prompt)
    full_prompt = "n".join(f"{.git,README.md,app.py,modules,requirements.txt,utils_chat.py}" mole': montent'" for m in history)
    full_prompt += "\nassistant:"

    try:
        response = client.text_generation(
            full_prompt,
            max_new_tokens=300,
            temperature=0.7,
            stop=ser:", "assistant:"{.git,README.md,app.py,modules,requirements.txt,utils_chat.py}" e"

    history.append({.git,README.md,app.py,modules,requirements.txt,utils_chat.py} "role": "assistant", "content": answer)
    return answer
