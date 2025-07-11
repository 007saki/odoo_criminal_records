# website_livechat_ai

This folder contains the Odoo module code that enables AI-powered livechat for website visitors.

## Features

- Integrates Odoo's built-in livechat with a local Ollama/Mistral AI model.
- Automatically responds to visitor messages using AI.
- Uses Python backend logic to call the AI model and post replies as OdooBot.

## How it works

1. When a visitor sends a message in the website livechat, Odoo intercepts it in the backend.
2. The message is sent to the local Ollama/Mistral AI model via HTTP API.
3. The AI's response is posted back to the chat, visible to the visitor.

## Key files

- `models/discuss_channel.py`: Extends Odoo's livechat channel to add AI response logic.
- `models/ai_chat.py`: Utility for connecting to the Ollama/Mistral API and getting AI replies.

## Requirements

- Odoo 18
- Ollama/Mistral running locally (`http://localhost:11434`)
- Python `requests` library installed

## Setup

1. Ensure Ollama/Mistral is installed and running.
2. Place the module files in your Odoo addons directory.
3. Restart Odoo and install/upgrade the module.

## Usage

- Visitors can chat on your website as usual.
- The AI will automatically reply to their messages in the chatbox.
