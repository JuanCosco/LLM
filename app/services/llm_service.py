import cohere

class LLMService:

    def __init__(self, api_key: str):
        self.client = cohere.Client(api_key)

    def analyze_text(self, text: str) -> str:
        message=f"""
Analiza el siguiente texto y determina si describe
una tarea repetitiva o automatizable en una empresa.

Texto:
{text}

Devuelve una explicación breve.
"""
        response = self.client.chat(
            model="command-r-08-2024",
            message=message
        )

        return response.text