import os
from huggingface_hub import InferenceClient

token = os.getenv("HF_TOKEN")
if not token:
    raise ValueError("⚠️ Variable d’environnement HF_TOKEN manquante.")

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    token=token
)

def init_chat():
    return [{"role": "system", "content": "Tu es un assistant IA francophone, clair et pertinent."}]

def ask(prompt, history):
    history.append({"role": "user", "content": prompt})
    full_prompt = "\n".join(f"{m['role']}: {m['content']}" for m in history)
    full_prompt += "\nassistant:"

    try:
        response = client.text_generation(
            prompt=full_prompt,
            max_new_tokens=300,
            temperature=0.7,
            stop=["user:", "assistant:"]
        )
        answer = response.strip().split("assistant:")[-1].strip()
    except Exception as e:
        answer = f"❌ Erreur IA : {e}"

    history.append({"role": "assistant", "content": answer})
    return answer
