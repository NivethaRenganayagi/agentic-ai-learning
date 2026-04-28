from openai import OpenAI

client = OpenAI(api_key="your_api_key")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "What is Agentic AI?"}
    ]
)

print(response.choices[0].message.content)
