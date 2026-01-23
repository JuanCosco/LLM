import json
import cohere

class LLMService:

    def __init__(self, api_key: str):
        self.client = cohere.Client(api_key)

    def analyze_text(self, text: str) -> str:
        message=f"""
Analiza el siguiente texto que describe un proceso empresarial.

Devuelve EXCLUSIVAMENTE un JSON válido con esta estructura:

{{
  "is_repetitive": boolean,
  "automation_potential": "low" | "medium" | "high",
  "justification": string
}}

Texto:
{text}
"""
        response = self.client.chat(
            model="command-r-08-2024",
            message=message,
            temperature=0
        )

        return json.loads(response.text)