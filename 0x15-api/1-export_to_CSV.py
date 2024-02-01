#!/usr/bin/python3
'''
Module contains python script for making an api call and writing response to
csv file
'''
import csv
import requests
import sys


if __name__ == '__main__':

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(user_id)
    todos_url = url + 'todos'
    user = requests.get(url).json()
    todos = requests.get(todos_url).json()

    dict_list = []
    for todo in todos:
        new_dict = {}
        new_dict['userId'] = user.get('id')
        new_dict['username'] = user.get('username')
        new_dict['completed'] = todo.get('completed')
        new_dict['title'] = todo.get('title')
        dict_list.append(new_dict)

    file_name = '{}.csv'.format(user.get('id'))

    with open(file_name, mode='w') as csv_file:
        fieldnames = ['userId', 'username', 'completed', 'title']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quotechar='"',
                                quoting=csv.QUOTE_ALL)

        for dict in dict_list:
            writer.writerow(dict)
