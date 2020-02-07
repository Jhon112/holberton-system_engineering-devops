#!/usr/bin/python3
"""
Use reddit API
"""
import requests


def top_ten(subreddit):
    """
    Get 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {
        'User-Agent': 'My user 1.0'
    }

    request = requests.get(url, headers=header, params={'limit': 10})
    if request.status_code == 404:
        print("None")
    else:
        data = request.json().get("data")
        children = data.get("children")
        for post in children:
            print(post.get("data")["title"])
