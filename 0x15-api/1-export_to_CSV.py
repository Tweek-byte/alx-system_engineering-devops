#!/usr/bin/python3
"""Exports TODO list into .csv"""
import csv
import requests
import sys


def export_to_csv(employee_id):
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

    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow(
                    [employee_id, username, t.get(
                        "completed"), t.get("title")])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
