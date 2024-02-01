#!/usr/bin/python3
'''
Module contains a function that makes an api call
'''
import requests


def top_ten(subreddit):
    '''
    Makes an api call to get the top ten hot posts in a given subreddit
    Args:
        subreddit(str) - The name of the subreddit to check
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    data = requests.get(url, headers={'User-agent': 'my-bot'},
                        allow_redirects=False)
    if data.status_code == 200:
        post_list = data.json().get('data').get('children')
        count = 0
        for post in post_list:
            if count == 10:
                break
            print(post.get("data").get("title"))
            count = count + 1
    else:
        print("None")
