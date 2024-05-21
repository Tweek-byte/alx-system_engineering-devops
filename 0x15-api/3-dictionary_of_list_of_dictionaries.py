#!/usr/bin/python3
import json
import requests
"""Exports TODO info to JSON format"""

def fetch_data():
    """Exports data in the JSON format"""
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    return users, todos


def export_to_json(users, todos):
    """Exports data to a JSON file."""
    data = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = []
        for task in todos:
            if task['userId'] == user_id:
                task_info = {
                    'username': username,
                    'task': task['title'],
                    'completed': task['completed']
                }
                user_tasks.append(task_info)
        data[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    users, todos = fetch_data()
    export_to_json(users, todos)
