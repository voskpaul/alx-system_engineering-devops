#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """query a subreddit and retrive top 10 posts"""
    # Reddit API endpoint for getting subreddit informatiom
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid too many requests error
    headers = {'User-Agent': 'My user Agent 1.0'}

    # send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # parse JSON response to extract no of subscribers(data field)
        data = response.json().get('data', {})
        children = data.get('children', [])
        for child in children[:10]:
            print(child.get('data', {}).get('title', ''))
    else:
        print(None)
