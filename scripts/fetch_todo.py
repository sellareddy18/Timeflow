from notion_client import Client
from pprint import pprint 
import json
from dotenv import load_dotenv 
import os 

load_dotenv() 
notion = Client(auth=os.getenv('NOTION_TOKEN'))

database_id=os.getenv('NOTION_DATABASE_ID')

def write_dict_to_file_as_json(content, file_name):
    content_as_json_str = json.dumps(content)

    with open(file_name, 'w') as f:
        f.write(content_as_json_str)


db_info = notion.databases.retrieve(database_id=database_id)
write_dict_to_file_as_json(db_info, "db_info.json")
