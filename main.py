from dotenv import load_dotenv
import os
from notion_client import Client

# python scripts
from scripts.welcome import welcome

load_dotenv()
notion = Client(auth=os.getenv('NOTION_TOKEN'))

users = notion.users.list()
user_name = users['results'][0]['name']

welcome(name=user_name)