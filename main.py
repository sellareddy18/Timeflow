from dotenv import load_dotenv
import os
from notion_client import Client
import time

# python scripts
from scripts.welcome import welcome
from scripts.fetch_todo import fetch_tasks_from_db

load_dotenv()
notion = Client(auth=os.getenv('NOTION_TOKEN'))

users = notion.users.list()
user_name = users['results'][0]['name']

welcome(name=user_name)
time.sleep(1)
fetch_tasks_from_db()