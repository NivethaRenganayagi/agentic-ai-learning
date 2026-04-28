from openai import OpenAI
import os

# Read config
api_key = os.getenv("NVIDIA_API_KEY")
model_name = os.getenv("MODEL_NAME", "meta/llama-3.1-70b-instruct")

# Create client
client = OpenAI(
    api_key=api_key,
    base_url="https://integrate.api.nvidia.com/v1"
)

print("\n=== Agentic AI Interactive Demo (with memory) ===")
print("Type 'exit' to quit\n")

# Store conversation history
messages = []

# Loop
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting...")
        break

    # Add user message
    messages.append({"role": "user", "content": user_input})

    # Call LLM
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    # Extract reply
    reply = response.choices[0].message.content

    # Print nicely
    print("\n=== AGENT RESPONSE ===\n")
    print(reply)
    print("\n======================\n")

    # Save assistant response (memory)
    messages.append({"role": "assistant", "content": reply})
