import json
import requests

class OpenRouter():
    def __init__(self):
        self.history = []
        pass


    def configure(self, api_key: str, model: str, pre_context: str, Temperature: float, Max_tokens: int, title_chat: str):
        
        self.url = "https://openrouter.ai/api/v1/chat/completions"

        self.headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",

        # opcionais:
        #"HTTP-Referer": "https://seusite.com",
        "X-Title": f"{title_chat}"
        }

        self.config = {
            "model": f"{model}",
            "temperature": Temperature,
            "max_tokens": Max_tokens,
            "system": pre_context
            # ativa resposta em streaming (opcional)
            # "stream": False

            }
        pass

    def request(self, msg: str):

        self.history.append({
            "role": "user",
            "content": msg

        })

    
        data = {
            "model": self.config["model"],

            "messages": [
                {
                    "role": "system",
                    "content": self.config["system"]
                },
                ] + self.history,

                "temperature": self.config["temperature"],
                "max_tokens": self.config["max_tokens"]
        }


        response = requests.post(
            url=self.url,
            headers=self.headers,
            json=data
        )

        message = response.json()["choices"][0]["message"]

        self.history.append(message)
        
        return message["content"]