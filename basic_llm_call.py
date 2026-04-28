from openai import OpenAI
import os

# Create client for NVIDIA NIM
client = OpenAI(
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1"
)

response = client.chat.completions.create(
    model="meta/llama3-70b-instruct",
    messages=[
        {"role": "user", "content": "What is Agentic AI?"}
    ],
    temperature=0.7,
    max_tokens=200
)

print(response.choices[0].message.content)
