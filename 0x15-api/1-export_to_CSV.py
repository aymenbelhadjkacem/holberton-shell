#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""
import csv
import requests
import sys


def fetch_api():
    """ extract data from api """
    user_i = sys.argv[1]
    url_info = "https://jsonplaceholder.typicode.com/users/{}/".format(
        user_i)
    response = requests.get(url_info).json()
    user_name = response.get("username")
    url_todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_i)
    todos = requests.get(url_todo).json()
    file_name = "{}.csv".format(user_i)
    with open('{}'.format(file_name), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [user_i, user_name, str(todo.get("completed")),
                    todo.get("title")]
                )


if __name__ == "__main__":
    fetch_api()
