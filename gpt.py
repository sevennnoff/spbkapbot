from openai import AsyncOpenAI
import asyncio
client = AsyncOpenAI(
    api_key="Апикей",
    base_url="https://api.proxyapi.ru/openai/v1",
    )

async def get_answer(text):
    print(text)
    prompt = "Ты - чат бот помощник колледжа автоматизации производства (Санкт-Петербург). Сайт колледжа: https://spbkap.ru. Отвечай только на вопросы, касающиеся колледжа, остальные игнорируй. Ответь на вопрос человека, который хочет в него поступить:" + text
    completion = await client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        model="gpt-4o-mini"
    )
    print(completion.choices[0])
    return completion.choices[0].message.content
