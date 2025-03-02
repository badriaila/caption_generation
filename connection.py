from openai import OpenAI
import os
from dotenv import load_dotenv
import base64

load_dotenv()


class Connection:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

    def __connect(self):
        return OpenAI(api_key=self.api_key)

    def __generate_caption(self, image_path):

        with open (image_path, "rb") as image_file:
            image_data = image_file.read()
            print(image_data)

        client = self.__connect()
        completion = client.chat.completions.create(
            model = "gpt-4o-mini",
            store = True,
            messages = [
                {"role": "system", "content": "You are an AI assistant describing indoor images for blind individuals."},
                {"role": "user", "content": f"Describe the image in less than 20 words: data:image/jpeg;base64, {base64.b64encode(image_data).decode()}"},
            ],
            max_tokens = 50,
            temperature = 0.5,
        )
        return completion.choices[0].message.content.strip()
    
    def generate(self, image_path):
        return self.__generate_caption(image_path)