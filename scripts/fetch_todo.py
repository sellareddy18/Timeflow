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

def safe_get(data, dot_chained_keys):
    '''
        {'a': {'b': [{'c': 1}]}}
        safe_get(data, 'a.b.0.c') -> 1
    '''
    keys = dot_chained_keys.split('.')
    for key in keys:
        try:
            if isinstance(data, list):
                data = data[int(key)]
            else:
                data = data[key]
        except (KeyError, TypeError, IndexError):
            return None
    return data

db_info = notion.databases.retrieve(database_id=database_id)

write_dict_to_file_as_json(db_info, "db_info.json")

db_rows = notion.databases.query(database_id=database_id) 
write_dict_to_file_as_json(db_rows, "db_rows.json")

def fetch_tasks_from_db():
    for row in db_rows['results']:
        task = safe_get(row, 'properties.Tasks.title.0.plain_text')
        due_data = safe_get(row, 'properties.Due Date.date.start')
        priority = safe_get(row, 'properties.priority.select.name')
        status = safe_get(row, 'properties.Status.status.name')
        est = safe_get(row, 'properties.Estimated time needed.rich_text.0.plain_text')
        
        print(f"Task: {task}, Due Date: {due_data}, Priority: {priority}, Status: {status}, Est: {est}")
