from notion_client import Client
from pprint import pprint
import json
from dotenv import load_dotenv
import os
from datetime import datetime
import time

load_dotenv()
notion = Client(auth=os.getenv('NOTION_TOKEN'))

database_id = os.getenv('NOTION_DATABASE_ID')

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
    todos = []
    for row in db_rows['results']:
        task = safe_get(row, 'properties.Tasks.title.0.plain_text')
        due_date = safe_get(row, 'properties.Due Date.date.start')
        priority = safe_get(row, 'properties.priority.select.name')
        status = safe_get(row, 'properties.Status.status.name')
        est = safe_get(row, 'properties.Estimated time needed.rich_text.0.plain_text')
        
        est_time = float(est) if est else float('inf')
        due_date_parsed = datetime.strptime(due_date, '%Y-%m-%d') if due_date else datetime.max

        todos.append({
            'task': task,
            'due_date': due_date,
            'priority': priority,
            'status': status,
            'est_time': est_time
        })

    # sort todos based on priority and estimated time needed
    priority_order = {'High': 1, 'Medium': 2, 'Low': 3}  # Customize this based on your priority levels
    todos.sort(key=lambda x: (priority_order.get(x['priority'], 4), x['due_date'], x['est_time']))

    print("Sorting tasks based on priority, due date, and estimated time needed.... 🤖")
    time.sleep(1)
    for task in todos:
        print(f"Task: {task['task']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Status: {task['status']}, Est: {task['est_time']}")

