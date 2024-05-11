from random import choice
import json
import requests

def get_response(user_input: str, author: str) -> str:
    lowered: str = user_input.lower()

    if lowered.startswith('!'):
        return None

    if lowered == '':
        return 'Absolute silence'
    elif 'hello' in lowered:
        return f'Hello there, {author}!'
    else:
        return choice(['I do not understand', 'What are you talking about?', 'Do you mind rephrasing that?'])

def load_challenges() -> list:
    try:
        with open('challenges.json','r') as json_file:
            json_data = json.load(json_file)
            challenges = json_data['challenges']
            return challenges
    except FileNotFoundError:
        print("Could not find 'challenges.json'")
        return []
    except json.JSONDecodeError as e:
        print("Error decoding JSON: {e}")
        return []

def random_challenge() -> dict:
    try:
        with open('challenges.json', 'r') as file:
            data = json.load(file)
            challenges = data['challenges']
            if challenges:  # Make sure the list is not empty
                return choice(challenges)
            else:
                return {"name": "No challenges available", "url": "#"}
    except FileNotFoundError:
        return {"name": "No challenges found", "url": "#"}
    except json.JSONDecodeError:
        return {"name": "Error loading challenges", "url": "#"}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"name": "Error retrieving a challenge", "url": "#"}

def random_quote() -> str:
    url = 'https://dummyjson.com/quotes/random'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX, 5XX)
        data = response.json()  # Convert the response to JSON
        quote = data.get('quote', 'No quote found')
        author = data.get('author', 'Unknown author')
        return f'"{quote}" - {author}'
    except requests.RequestException as e:
        return f"Failed to retrieve quote: {e}"

def add_challenge(name: str, url: str) -> str:
    expected_url_syntax = "https://codingchallenges.fyi/challenges/"

    if not url.startswith(expected_url_syntax):
        return f"Unable to add: {url} Please check if it is a valid Coding Challenge"

    try:
        with open('challenges.json', 'r+') as file:
            data = json.load(file)
            challenges = data.get('challenges', [])

            if any(challenge['url'] == url for challenge in challenges):
                return "Challenge with this URL already exists."

            # Add the new challenge
            challenges.append({"name": name, "url": url})
            data['challenges'] = challenges

            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

            return f"Added: {name} : {url}"
    except FileNotFoundError:
        return "Failed to find 'challenges.json'. Please check the file path."
    except json.JSONDecodeError:
        return "Error loading JSON data. Please check the integrity of the 'challenges.json'."
    except Exception as e:
        return f"An unexpected error occurred: {e}"