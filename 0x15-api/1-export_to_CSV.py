#!/usr/bin/python3
"""Script that takes an employee id as an argument and returns their info using
the JSON placeholder API."""

from csv import DictWriter, QUOTE_ALL
from requests import get
from sys import argv


def main():
    """Main function that prints information about the employee."""
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{main_url}/user/{sys.argv[1]}/todos"
    name_url = f"{main_url}/users/{sys.argv[1]}"
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    todo_list = []
    for todo in todo_result:
        todo_dict = {}
        todo_dict.update({"user_ID": argv[1], "username": name_result.get(
            "username"), "completed": todo.get("completed"),
                        "task": todo.get("title")})
        todo_list.append(todo_dict)
    with open("{}.csv".format(argv[1]), 'w', newline='') as f:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(todo_list)


if __name__ == '__main__':
    main()
