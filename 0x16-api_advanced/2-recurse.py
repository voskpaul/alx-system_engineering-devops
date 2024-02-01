#!/usr/bin/python3
'''
Module contains a function that makes an api call
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''
    Makes an api call to get the top ten hot posts in a given subreddit
    Args:
        subreddit(str) - The name of the subreddit to check
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    data = requests.get(url, headers={'User-agent': 'my-bot'},
                        params={'after': after}, allow_redirects=False)

    if data.status_code == 200:
        after = data.json().get('data').get('after')
        post_list = data.json().get('data').get('children')

        for post in post_list:
            hot_list.append(post.get("data").get("title"))

        if after is None:
            # If there is no new page
            if len(hot_list) == 0:
                return None

            return hot_list
        else:
            # If there is another page
            return recurse(subreddit, hot_list, after)
    else:
        return None
