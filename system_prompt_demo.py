from openai import OpenAI

client = OpenAI(api_key="your_api_key")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful teacher"},
        {"role": "user", "content": "Explain ReAct loop"}
    ]
)

print(response.choices[0].message.content)
