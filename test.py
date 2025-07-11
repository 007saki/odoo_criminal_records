import requests

def get_ai_reply_ollama(prompt, model="mistral", host="http://localhost:11434"):
    try:
        response = requests.post(
            f"{host}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )
        if response.ok:
            data = response.json()
            return data.get("response") or data.get("message") or str(data)
        else:
            return f"AI error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"AI error: {e}"

# Test the function manually
if __name__ == "__main__":
    user_input = input("Ask AI: ")
    reply = get_ai_reply_ollama(user_input)
    print("AI Reply:", reply)
