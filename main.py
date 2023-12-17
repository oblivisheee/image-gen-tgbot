import telebot
from api import generate_image, save_image
import os
from config import BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, I am a special utility for generating images. Just write a prompt and I'll generate an image.")

@bot.message_handler(content_types=['text'])
def generate(message):
    prompt = message.text
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, 'Generating your image...')
    image_url = generate_image(prompt)
    image_path = os.path.join(os.getcwd(), 'image.jpg')
    save_image(image_url, image_path)
    bot.send_chat_action(message.chat.id, 'upload_photo')  # Set status as 'upload_photo'
    with open(image_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    os.remove(image_path)
    bot.send_message(message.chat.id, 'Your image has been generated!')

bot.polling(non_stop=True)

