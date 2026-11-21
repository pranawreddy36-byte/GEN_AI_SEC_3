import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found! Add it to your .env file.")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5.5",
    input="What is Artificial Intelligence? Explain in simple words."
)

print("\nLLM Response:")
print(response.output_text)
