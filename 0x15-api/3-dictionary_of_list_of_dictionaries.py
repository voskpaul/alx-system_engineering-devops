#!/usr/bin/python3

"""export data in the JSON format"""


from urllib import request
from sys import argv
from requests import *
import json


if __name__ == "__main__":
    """export data in the JSON format"""

    # send a request to retrieve all users
    url = "https://jsonplaceholder.typicode.com/users"
    response = get(url)

    # extract all users from response
    users = response.json()

    # create a dictionary to store all tasks for all employees
    all_tasks = {}

    # loop through all users
    for user in users:
        # retrieve user ID and username
        user_id = user.get("id")
        username = user.get("username")

        # send a request to retrieve user's todo list
        url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
               .format(user_id))

        # store the response from the api in response variable
        response = get(url)

        # extract todo list from response
        todo_list = response.json()

        # create a list of tasks for the user
        tasks = []
        for task in todo_list:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            tasks.append(task_dict)

        # add the list of tasks to the dictionary
        all_tasks[user_id] = tasks

    # export the data to json format
    with open("todo_all_employees.json", "w") as file:
        json.dump(all_tasks, file)

