# brave-leo

Use the Leo AI assistant by Brave anywhere!

## Getting Started:

    python main.py

## Example:

```python
from main import Leo
from asyncio import run


async def main():
    while True:
        prompt = input("👦: ")
        try:
            leo = Leo("qztbjzBqJueQZLFkwTTJrieu8Vw3789u")
            resp = await leo.generate(prompt)
            print(f"🤖: {resp}")
        except Exception as e:
            print(f"🤖: {e}")


run(main())
```

## Credits:

-   [KohnoseLami/Brave-Leo](https://github.com/KohnoseLami/Brave-Leo)