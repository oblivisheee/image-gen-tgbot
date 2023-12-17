# Image-Gen-TgBot

This is a Telegram bot that generates images based on the text prompts you provide. It utilizes the OpenAI API to generate these images.

## Installation

1. Clone this repository.
2. Install the required Python packages using the provided `requirements.txt` file. This can be accomplished by running the `install.sh` script: 
```bash
./install.sh
```


## Configuration

Before you can utilize the bot, you need to set up your API keys. These should be set in the `config.py` file:
```python
BOT_TOKEN ='YOUR_TELEGRAM_BOT_TOKEN'
OPENAI_API = 'YOUR_OPENAI_API_KEY'
```

Replace `'YOUR_TELEGRAM_BOT_TOKEN'` and `'YOUR_OPENAI_API_KEY'` with your actual API keys.

## Usage

To initiate the bot, use:
```bash
./start.sh
```

To generate an image, write into the bot prompt, and you'll receive a result.
