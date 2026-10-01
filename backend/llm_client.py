from groq import AsyncGroq
from backend.config import GROQ_API_KEY, MODEL_NAME


class LLMClient:

    async def generate(self, messages):
        client = AsyncGroq(api_key=GROQ_API_KEY)

        response = await client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7
        )

        return response.choices[0].message.content
