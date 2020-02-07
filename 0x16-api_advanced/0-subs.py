#!/usr/bin/python3
"""
Use reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get all subscribers for a subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        'User-Agent': 'My user 1.0'
    }

    request = requests.get(url, headers=header)
    if request.status_code == 404:
        return 0
    data = request.json().get("data")
    return data.get("subscribers")
