from openai import OpenAI

client = OpenAI(
    api_key="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"
    base_url="https://integrate.api.nvidia.com/v1"
)

response = client.chat.completions.create(
    model="meta/llama3-70b-instruct",
    messages=[
        {"role": "user", "content": "Explain Agentic AI"}
    ]
)

print(response.choices[0].message.content)
