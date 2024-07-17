import requests
import time

response = requests.get("https://type.fit/api/quotes")

data = response.json()
inspirational_text = data[0]["text"]
author = data[0]["author"]
modified_author = author.replace(", type.fit", '')

def welcome(name):
    print(f'"{inspirational_text}" - {modified_author}')
    time.sleep(2)
    print(f"Welcome to Timeflow: {name}")
    time.sleep(2)
    while True: 
        user_input = input("Are you ready to schedule your day? (Y for yes, N: for no): ")
        if user_input == "Y":
            print("Amazing 🥳")
            break
        elif user_input == "N":
            print("That's okay let us know when you are ready.")
            time.sleep(300) # sleeps for 5 minutes and then responds with the same question
        else: 
            print("Invalid input please respond with a Y or N")

    if user_input == "Y": 
        print("fetching todos from database")
        # run function here
        print("fetched the todos")