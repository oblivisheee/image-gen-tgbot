from openai import OpenAI
from config import OPENAI_API
import requests
import os

def generate_image(prompt):
    client = OpenAI(base_url='https://api.naga.ac/v1', api_key=OPENAI_API)
    response = client.images.generate(
        model="sdxl",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url

def save_image(url, path):
    response = requests.get(url)
    with open(path, 'wb') as file:
        file.write(response.content)
if __name__ == '__main__':
    image_url = generate_image("a white siamese cat")
    save_image(image_url, os.path.join(os.getcwd(), 'image.jpg'))
