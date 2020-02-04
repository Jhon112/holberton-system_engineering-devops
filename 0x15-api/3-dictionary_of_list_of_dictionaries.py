#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_url = 'https://jsonplaceholder.typicode.com/users'
    r_user = requests.get(user_url)
    users = r_user.json()
    data_list = {}

    for user in users:
        user_id = user.get('id')
        todo_url = 'https://jsonplaceholder.typicode.com/todos'

        r_todos = requests.get(todo_url, params={'userId': user_id})
        todos = r_todos.json()
        data_list[user_id] = [
            {
                'task': todo.get('title'),
                'completed': todo.get('completed'),
                'username': user.get('username'),
            }
            for todo in todos
        ]

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data_list, json_file, indent=2)
