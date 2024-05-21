#!/usr/bin/python3
import json
import requests

def fetch_data():
    """
    Fetches user and todo data from the JSONPlaceholder API.

    Returns:
        tuple: A tuple containing lists of users and todos.
    """
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    return users, todos

def export_to_json(users, todos):
    """
    Organizes the fetched data into a dictionary and exports it to a JSON file.

    Args:
        users (list): List of user dictionaries.
        todos (list): List of todo dictionaries.
    """
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

