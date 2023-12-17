# Image-Gen-TgBot

This is a Telegram bot that generates images based on the text prompts you provide. It leverages the OpenAI API to generate these images.

## Installation

1. Clone this repository.
2. Install the required Python packages using the provided `requirements.txt` file. This can be done by executing the `install.sh` script: 
```bash
sudo bash install.sh
```

## API

This bot uses the NagaAI API. To obtain the API key, visit their [discord server](https://discord.gg/dZpCWZ3d) and use the following command to get your API key:
```
/key get

```

## Configuration

Before you can use the bot, you need to configure your API keys. These should be set in the `config.py` file:
```python
BOT_TOKEN ='YOUR_TELEGRAM_BOT_TOKEN'
OPENAI_API = 'YOUR_OPENAI_API_KEY'
```

Replace `'YOUR_TELEGRAM_BOT_TOKEN'` and `'YOUR_OPENAI_API_KEY'` with your actual API keys.

## Usage

To start the bot, execute:
```bash
sudo bash start.sh
```

To generate an image, type your prompt into the bot, and you'll receive the generated image.
