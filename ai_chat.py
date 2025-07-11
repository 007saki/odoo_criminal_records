# ai_chat.py
import requests

def get_ai_reply_ollama(prompt, model="mistral", host="http://localhost:11434"):
    try:
        response = requests.post(
            f"{host}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=60
        )
        if response.ok:
            return response.json().get("response", "...")
        else:
            return f"AI error: {response.status_code} {response.text}"
    except Exception as e:
        return f"AI error: {e}"
