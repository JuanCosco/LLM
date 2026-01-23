import cohere

class LLMService:

    def __init__(self, api_key: str):
        self.client = cohere.Client(api_key)

    def analyze_text(self, text: str) -> str:
        response = self.client.chat(
            model="command-r-08-2024",
            message=f"Explícame qué es una API en pocas palabras.\n\nTexto:\n{text}"
        )

        return response.text