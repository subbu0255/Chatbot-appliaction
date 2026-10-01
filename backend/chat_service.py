from backend.llm_client import LLMClient


class ChatService:

    def __init__(self):
        self.llm_client = LLMClient()

    async def get_response(self, message, history):
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant. "
                    "Give clear and beginner-friendly answers."
                )
            }
        ]

        messages.extend(history)

        messages.append(
            {
                "role": "user",
                "content": message
            }
        )

        answer = await self.llm_client.generate(messages)

        return answer
