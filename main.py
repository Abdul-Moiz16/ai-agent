import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

if os.environ.get("OPENROUTER_API_KEY") == None:
    raise RuntimeError("OPENROUTER_API_KEY is not set in the environment variables. Please set it in the .env file.")
else: 
    api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": args.user_prompt
        }
    ],
)


def main():
    print("Hello from ai-agent!")
    if response.usage == None:
        raise RuntimeError("Response usage is None. Please check your API key and model availability.")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print(f"Response: {response.choices[0].message.content}")



if __name__ == "__main__":
    main()
