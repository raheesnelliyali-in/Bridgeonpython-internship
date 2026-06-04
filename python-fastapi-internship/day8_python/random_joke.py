import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    joke = response.json()

    print("😂 Random Joke")
    print("-" * 30)
    print("Setup:", joke["setup"])
    print("Punchline:", joke["punchline"])
else:
    print("Failed to fetch joke.")