import requests
import json
import os

LOCAL_API_URL = os.getenv("LOCAL_LLM_URL", "http://localhost:8080/v1")
LOCAL_MODEL = os.getenv("LOCAL_LLM_MODEL", "Marlon81/Phi-3-mini-4k-instruct-Q5_K_M-GGUF:Q5_K_M")

url = f"{LOCAL_API_URL}/chat/completions"

print("Chatbot iniciado. Escribe 'exit' para salir.\n")

while True:
    user_input = input("Tú: ")
    if user_input.lower() == "exit":
        print("¡Hasta luego!")
        break

    try:
        payload = {
            "model": LOCAL_MODEL,
            "messages": [{"role": "user", "content": user_input}],
            "stream": False
        }
        response = requests.post(url, json=payload, timeout=120)
        if response.status_code == 200:
            result = response.json()
            print(f"Bot: {result['choices'][0]['message']['content']}\n")
        else:
            print(f"Error: {response.status_code} - {response.text}\n")
    except requests.exceptions.ConnectionError:
        print("Error: No se puede conectar al servidor.\n")
    except Exception as e:
        print(f"Error: {e}\n")