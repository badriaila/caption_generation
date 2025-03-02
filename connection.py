from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


class Connection:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

    def connect(self):
        return OpenAI(api_key = self.api_key)


connection = Connection()

client = connection.connect()

completion = client.chat.completions.create(
    model = "gpt-4o-mini",
    store = True,
    messages = [
        {"role": "user", "content": "Explain generative AI in 20 words or less."},
    ]
)

print(completion.choices[0].message)