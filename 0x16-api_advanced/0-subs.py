#!/usr/bin/python3

"""
Model working with Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    Gets the number of subscribers of reddit
    """
    headers = {"User-Agent": 'my_bot/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
