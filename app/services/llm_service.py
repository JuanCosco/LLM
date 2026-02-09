import cohere
import asyncio
import json

class LLMService:

    def __init__(self, api_key):
        self.client = cohere.Client(api_key)

    def analyze_process_sync(self, text: str):

        response = self.client.chat(
            model="command-r-08-2024",
            message=f"""
Analiza el siguiente texto y responde SOLO en formato JSON.
NO incluyas texto adicional, ni explicaciones, ni markdown.

Campos:
- received_text (string)
- is_repetitive (true/false)
- automation_potential (0-10)
- justification (string)

Texto:
{text}
"""
    )

        raw = response.text.strip()
    
        if raw.startswith("```"):
            raw = raw.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(raw)
        except json.JSONDecodeError:
        # logging defensivo (muy importante)
            return {
                "received_text": text,
                "is_repetitive": False,
                "automation_potential": 0,
                "justification": "Error parsing LLM response"
        }


    async def analyze_process(self, text: str):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            None,
            self.analyze_process_sync,
            text
            )