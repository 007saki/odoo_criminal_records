import requests

def get_ai_reply_ollama(prompt, model="mistral", host="http://localhost:11434"):
    try:
        response = requests.post(
            f"{host}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=(10, 600)  # Connect timeout, read timeout
        )
        if response.ok:
            data = response.json()
            return data.get("response", "No response.")
        else:
            return f"AI error: {response.status_code} {response.text}"
    except Exception as e:
        return f"AI error: {e}"
