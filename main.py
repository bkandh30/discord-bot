from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response, load_challenges, random_challenge, random_quote, add_challenge
from bs4 import BeautifulSoup
import requests

#load our discord token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#bot setup
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

#message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled properly)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message, message.author)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

#handling bot startup
@client.event
async def on_read()-> None:
    print(f'{client.user} is now running!')

#fetch the title from the coding challenge url
def fetch_title(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('title')

        return title_tag.text.strip() if title_tag else "No title found"
    except requests.RequestException as e:
        return f"Failed to retrieve URL: {e}"

#handling the incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    if message.content.startswith('!'):
        if message.content == '!list':
            challenges = load_challenges()
            response = "\n".join([f"{ch['name']}: {ch['url']}" for ch in challenges])
            await message.channel.send(response)
            return
        elif message.content == '!quote':
            response = random_quote()
            await message.channel.send(response)
            return
        elif message.content == '!info':
            response = 'Made by Bhavya Kandhari'
            await message.channel.send(response)
            return
        elif message.content == '!challenge':
            challenge = random_challenge()
            response = f"{challenge['name']}: {challenge['url']}"
            await message.channel.send(response)
            return
        elif message.content.startswith('!add '):
            if message.content.startswith('!add '):
                url = message.content[len('!add '):].strip()
                if url.startswith('https://codingchallenges.fyi/challenges/'):
                    title = fetch_title(url)
                    result = add_challenge(title, url)
                    await message.channel.send(result)
                    return
                else:
                    await message.channel.send("URL must start with 'https://codingchallenges.fyi/challenges/'.")
                    return
        else:
            await message.channel.send("Unknown command")
            return

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

#main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()