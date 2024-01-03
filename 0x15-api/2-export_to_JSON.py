#!/usr/bin/python3
"""export data to json format"""

import csv
from urllib import request
from sys import argv
from requests import *
import json


if __name__ == "__main__":
    """export data in the CSV format"""
    # Retrieves the user ID from the first command-line argument
    user_id = argv[1]

    # send a request to retrieve user id
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    # store the response from the api in response variable
    response = get(url)

    # extract users username from response
    username = response.json().get("username")

    # send a request to retrieve user's todo list
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)

    # store the response from the api in response variable
    response = get(url)

    # extract todo list from response
    todo_list = response.json()

    # create json dictionary
    json_dict = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todo_list
        ]
    }
    # export the data to json format
    with open("{}.json".format(user_id), "w") as file:
        json.dump(json_dict, file)

