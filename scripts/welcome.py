import requests
import time

response = requests.get("https://type.fit/api/quotes")

data = response.json()
inspirational_text = data[0]["text"]
author = data[0]["author"]
modified_author = author.replace(", type.fit", '')

def welcome(name):
    print(f"{inspirational_text} - {modified_author}")
    time.sleep(1.5)
    print(f"Welcome to Timeflow: {name}")