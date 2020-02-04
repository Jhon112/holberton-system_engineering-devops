#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
r_user = requests.get(user_url)
user = r_user.json()

todo_url = 'https://jsonplaceholder.typicode.com/todos'
r_todos = requests.get(todo_url, params={'userId': user['id']})
todos = r_todos.json()

todos_completed = list(filter(lambda todo: todo if todo['completed'] is True
                       else None, todos))

print("Employee {} is done with tasks({}/{}):".format(
    user['name'], len(todos_completed), len(todos)
))

for todo_complete in todos_completed:
    print('\t{}'.format(todo_complete['title']))
