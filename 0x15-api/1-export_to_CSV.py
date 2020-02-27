#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import csv
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

    data_list = []
    for todo in todos:
        data_list.append({
            'userId': todo.get('userId'),
            'username': user.get('username'),
            'completed': todo.get('completed'),
            'title': todo.get('title'),
        })

    with open('{}.csv'.format(sys.argv[1]), mode='w', newline='') as csv_file:
        fieldnames = ['userId', 'username', 'completed', 'title']
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
            quoting=csv.QUOTE_ALL
        )

        for todo in data_list:
            writer.writerow(todo)
