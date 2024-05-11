# Build Your Own Discord Bot

This is my python solution to John Crickett's Coding Challenge: [Build Your Own Discord Bot](https://codingchallenges.fyi/challenges/challenge-discord)

## Description

This is a simple implementation of a Discord bot written in Python using (discord.py)[https://discordpy.readthedocs.io/en/stable/]

The bot supports the following functionalities:

- After the bot is added to a server and hosted, it will send to a `Hello` message sent by the client with the message `Hello there, <user-display-name>`.
- The following commands are implement

  - `!add`: This command takes a URL as an argument and adds a new coding challenge to the json file.
  - `!challenge`: Suggests a random challenge from the json file.
  - `!list`: Lists all the challenges available.
  - `!quote`: Fetch a random quote using https://dummyjson.com/quotes/random
  - `!info`: Fetches the creator information.

## Usage

Create a `.env` file at the root directory of this repository and add the following environment variables:

```bash
DISCORD_TOKEN='discord-token'
```

Go to the root directory of this repository and run the following command to start the discord bot:

```bash
python3 main.py
```
