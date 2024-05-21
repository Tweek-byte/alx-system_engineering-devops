#!/usr/bin/python3
"""Returns to-do list information per EID"""
import requests
import sys


def get_todo_list(employee_id):
    url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(url + f"users/{employee_id}")
    if user_response.status_code != 200:
        print("User not found")
        return

    user = user_response.json()

    todos_response = requests.get(
            url + "todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Error fetching todos")
        return

    todos = todos_response.json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for title in completed:
        print("\t {}".format(title))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_todo_list(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
