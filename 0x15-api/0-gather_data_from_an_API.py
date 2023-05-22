#!/usr/bin/python3
"""
Script that takes an employee id as an argument and returns their info using
the JSON placeholder API."""


import requests
import sys


def main():
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{main_url}/user/{sys.argv[1]}/todos"
    name_url = f"{main_url}/users/{sys.argv[1]}"
    todo_result = requests.get(todo_url).json()
    name_result = requests.get(name_url).json()


    todo_num = len(todo_result)
    todo_complete = len([todo for todo in todo_result if todo["completed"]])
    name = name_result["name"]
    print(f"Employee {name} is done with tasks({todo_complete}/{todo_num}):")
    for todo in todo_result:
        if todo["completed"]:
            print(f"\t {todo['title']}")


if __name__ == '__main__':
    main()
