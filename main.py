import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
# from functions.get_files_info import get_files_info

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"

def main():
    if len(sys.argv) < 2:
        print("Error: prompt not provided")
        sys.exit(1)

    flag = ""
    if len(sys.argv) > 2:
        flag = sys.argv[2]

    user_prompt = sys.argv[1]
    message = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(model=model, contents=message)
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    print(response.text)
    if flag == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()
