## Action for Happiness Bot

Gets the daily action from the [Action for Happiness website](https://actionforhappiness.org/).

---

## Installation

Run the following command to install required packages.

```
pip install -r requirements.txt
```

---

## Adding Environment Variables

An application and bot will need to be created in the [Discord Developer Portal](https://discord.com/developers/applications/).

Your env.py file will require two main bits of information:

- A Discord Bot Token.
- The ID of the server the bot is to be used on.

Please populate the env.py with these details:

```
import os

os.environ['DISCORD_TOKEN'] = 'YOUR_DISCORD_TOKEN_HERE'
os.environ['SERVER_ID'] = 'YOUR_DISCORD_SERVER_ID_HERE'
```

## Running the Bot

If your details have been added successfully you can run the bot with the command:

```
python app.py
```

or

```
python3 app.py
```

---

The bot should return a message confirming a successfull connection.

```
Action for Happiness Bot has connected to Discord!
```

---

## Inviting the Bot

The bot can be invited to your server by selecting it in the [Discord Developer Portal](https://discord.com/developers/applications/) and navigating to OAuth2 > URL Generator.

The bot should be given:

- Scope - Bot
- Permissions - Send Messages & Use Slash Commands

---

## Using the Bot

The bot can be used by typing the slash command /action into the chat.

It will then respond with the daily image within an embed, or an error message if the embed cannot be found.

---
