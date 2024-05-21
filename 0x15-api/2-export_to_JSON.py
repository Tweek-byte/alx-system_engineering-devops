#!/usr/bin/python3
"""Exports TODO list to .JSON"""
import json
import requests
import sys


def export_to_json(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + f"users/{employee_id}")
    if user_response.status_code != 200:
        print("User not found")
        return

    user = user_response.json()
    username = user.get("username")
    todos_response = requests.get(
            url + "todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Error fetching todos")
        return

    todos = todos_response.json()
    tasks = [{
        "task": t.get("title"),
        "completed": t.get("completed"),
        "username": username
    } for t in todos]

    data = {str(employee_id): tasks}

    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
