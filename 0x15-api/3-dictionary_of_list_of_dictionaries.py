#!/usr/bin/python3
'''
Module contains python script for making an api call and writing response to
csv file
'''
import json
import requests


if __name__ == '__main__':

    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    todos_dict = {}
    for user in users:
        user_todo_list = []
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                new_dict = {}
                new_dict['task'] = todo.get('title')
                new_dict['completed'] = todo.get('completed')
                new_dict['username'] = user.get('username')
                user_todo_list.append(new_dict)
        todos_dict[user.get('id')] = user_todo_list

    file_name = 'todo_all_employees.json'

    with open(file_name, mode='w') as outfile:
        json.dump(todos_dict, outfile)
