import argparse
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from functions.call_function import available_functions
from functions.call_function import call_function

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
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

def main():
    print("Hello from ai-agent!")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")

    for _ in range(20):
        response = client.chat.completions.create(
                    model="openrouter/free",
                    messages=messages,
                    temperature=0,
                    tools=available_functions,
                )
        if response.usage == None:
            raise RuntimeError("Response usage is None. Please check your API key and model availability.")
        if args.verbose:
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")

        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            print(f"Final response:\n{message.content}")
            return

        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)
            if result_message == None:
                raise Exception("Result message is None. Please check the function call and arguments.")
            if args.verbose:
                print(f"-> {result_message['content']}")
            messages.append(result_message)

    print("Error: Maximum iterations reached without a final response.")
    sys.exit(1)


if __name__ == "__main__":
    main()
