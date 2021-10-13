#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import json
import requests


def fetch_api():
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    userdict = {}
    usernamedict = {}
    for user in users:
        uid = user.get("id")
        userdict[uid] = []
        usernamedict[uid] = user.get("username")
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        verify=False).json()
    for todo in todos:
        taskdict = {}
        uid = todo.get("userId")
        taskdict["task"] = todo.get('title')
        taskdict["completed"] = todo.get('completed')
        taskdict["username"] = usernamedict.get(uid)
        userdict.get(uid).append(taskdict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(userdict, jsonfile)

if __name__ == '__main__':
    fetch_api()
