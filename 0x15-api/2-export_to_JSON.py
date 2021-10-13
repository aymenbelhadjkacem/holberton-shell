#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""
import json
import requests
from sys import argv


def fetch_api():
    """ extract data from api """
    try:
        user_i = int(argv[1])
    except ValueError:
        exit()
    url_info = "https://jsonplaceholder.typicode.com/users/{}/".format(
        user_i)
    response = requests.get(url_info).json()
    user_name = response.get("username")
    url_todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_i)
    todos = requests.get(url_todo).json()
    file_name = "{}.json".format(user_i)
    d = {}
    l = []
    for todo in todos:
        d1 = {}
        d1['task'] = todo.get('title')
        d1['completed'] = todo.get('completed')
        d1['username'] = user_name
        l.append(d1)
    d[user_i] = l
    # print(d)
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(d, f)

if __name__ == "__main__":
    fetch_api()
