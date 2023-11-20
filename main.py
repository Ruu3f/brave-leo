from json import dumps
from aiohttp import ClientSession, ClientError


class Leo:
    def __init__(self, x_brave_key):
        self.x_brave_key = x_brave_key

    async def generate(self, prompt):
        async with ClientSession() as session:
            async with session.post(
                url="https://ai-chat.bsg.brave.com/v1/complete",
                headers={
                    "x-brave-key": self.x_brave_key,
                    "content-type": "application/json",
                },
                data=dumps(
                    {
                        "max_tokens_to_sample": 600,
                        "model": "llama-2-13b-chat",
                        "prompt": f"<s>[INST] {prompt} [/INST]",
                        "stop_sequences": ["</response>", "</s>"],
                        "temperature": 0.2,
                        "top_k": -1,
                        "top_p": 0.999,
                    }
                ),
            ) as resp:
                try:
                    data = await resp.json()
                    return data["completion"]
                except ClientError as exc:
                    raise ClientError("Unable to fetch the response.") from exc
