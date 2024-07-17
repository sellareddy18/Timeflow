from dotenv import load_dotenv
import os
from notion_client import Client
from pprint import pprint


load_dotenv()
notion = Client(auth=os.getenv('NOTION_TOKEN'))

list_users_response = notion.users.list()
pprint(list_users_response)