#!/usr/bin/python3
"""Use reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    returns a list containing the titles of all
    hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {
        'User-Agent': 'My user 1.0'
    }
    request = requests.get(url, headers=header, params={
        "limit": 100,
        "after": after
    })

    if after is None:
        return hot_list

    if request.status_code == 404:
        return None

    response = request.json()
    for children in response.get("data").get("children"):
        hot_list.append(children.get("data").get("title"))

    after = response.get("data").get("after")
    return recurse(subreddit, hot_list, after)
