import telebot
from api import generate_image, save_image
import os
from config import BOT_TOKEN, LOG
from threading import Thread
bot = telebot.TeleBot(BOT_TOKEN, threaded=True)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, I am a special utility designed to generate images. Simply provide a prompt and I will generate an image for you. We are using the SDXL model, so please ensure your prompt is compatible with its model.")

@bot.message_handler(content_types=['text'])
def generate(message):
    Thread(target=generate_image_thread, args=(message,)).start()

def generate_image_thread(message):
    prompt = message.text
    user_id = message.from_user.id
    if LOG:
        print(f"#{user_id}@{message.from_user.username}: {prompt}")
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, 'Generating your image...')
    
    image_url = generate_image(prompt)
    if image_url is None:
        if LOG:
            print(f'Error occurred while processing the prompt from user #{user_id}@{message.from_user.username}. The error could be due to NSFW content or an issue with the API.')
        bot.send_message(message.chat.id, 'Something went wrong, possibly, that was an NSFW alert, or problem with API, try again please.')
        return
    
    image_path = os.path.join(os.getcwd(), f'{user_id}-image.jpg')
    save_image(image_url, image_path)
    bot.send_chat_action(message.chat.id, 'upload_photo')
    with open(image_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    os.remove(image_path)
    bot.send_message(message.chat.id, 'Your image has been generated!')

bot.polling(non_stop=True)

