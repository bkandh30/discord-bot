# 🤖 Build Your Own Discord Bot

A Python-based implementation of a custom Discord bot, developed as a solution to [John Crickett's Coding Challenge](https://codingchallenges.fyi/challenges/challenge-discord).

This project uses the [discord.py](https://discordpy.readthedocs.io/en/stable/) library to create an interactive bot that responds to user commands and messages within a Discord server.

## 📄 Features

Once added to a Discord server and successfully hosted, the bot offers the following functionalities:

### 🔹 Basic Interaction
- Responds to any `Hello` message with:
  ```
  Hello there, <user-display-name>
  ```

### 🔹 Commands

- `!add <url>`  
  Adds a new coding challenge (provided as a URL) to a local JSON file.

- `!challenge`  
  Suggests a random challenge from the stored list.

- `!list`  
  Lists all saved coding challenges.

- `!quote`  
  Fetches and displays a random quote using the [DummyJSON API](https://dummyjson.com/quotes/random).

- `!info`  
  Displays creator or bot information.


## ⚙️ Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone [https://github.com/<your-username>/discord-bot-challenge.git](https://github.com/bkandh30/discord-bot.git)
   cd discord-bot
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:

   Create a `.env` file in the root directory with the following content:

   ```bash
   DISCORD_TOKEN='your-discord-bot-token'
   ```

4. **Run the Bot**:

   ```bash
   python3 main.py
   ```

## ✅ Requirements

- Python 3.x
- `discord.py`
- `dotenv` (for environment variable management)

## 🧾 License

This project is licensed under the [MIT License](LICENSE).
