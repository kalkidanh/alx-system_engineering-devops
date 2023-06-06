#!/usr/bin/python3
"""A function that uses recursion to  query the Reddit API and returns a list
of the titles of all hot articles for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns the top ten post titles recursively."""
    headers = {'User-Agent': 'chrome 51.0.2704.106'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    arg = {'after': after}

    response = requests.get(url, params=arg, headers=headers)
    after = response.json().get("data").get("after")
    titles = response.json().get("data").get("children")

    if after:
        if titles:
            for i in titles:
                hot_list.append(i.get("data").get("title"))
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return (None)
