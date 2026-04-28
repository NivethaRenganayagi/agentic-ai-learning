from openai import OpenAI
import os

# Read API key and model from environment
api_key = os.getenv("NVIDIA_API_KEY")
model_name = os.getenv("MODEL_NAME", "meta/llama-3.1-70b-instruct")

# Create client for NVIDIA NIM
client = OpenAI(
    api_key=api_key,
    base_url="https://integrate.api.nvidia.com/v1"
)

# Make request
response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "user", "content": "What is Agentic AI?"}
    ],
    temperature=0.7,
    max_tokens=500   # increased token limit
)

# Pretty output
print("\n=== AGENT RESPONSE ===\n")
print(response.choices[0].message.content)
print("\n======================\n")
