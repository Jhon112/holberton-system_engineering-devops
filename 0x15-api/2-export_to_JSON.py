#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        sys.argv[1]
    )
    r_user = requests.get(user_url)
    user = r_user.json()

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    r_todos = requests.get(todo_url, params={'userId': user.get('id')})
    todos = r_todos.json()

    data_list = {
        '{}'.format(user.get('id')): []
    }
    for todo in todos:
        data_list.get('{}'.format(user.get('id'))).append(
        {
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': user.get('username'),
        }
        ) 

    with open('{}.json'.format(user.get('id')), 'w') as json_file:
        json.dump(data_list, json_file, indent=2)
