#!/usr/bin/python3
"""Function that queries the reddit API and returns the titles of
the first 10 posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """Returns the titles of the top 10 posts of the subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'chrome 51.0.2704.106'}
    params = {'limit': 10}
    response = requests.get(url, params=params, headers=headers).json()

    try:
        titles = response.get('data').get('children')

        for i in titles:
            print(i.get('data').get('title'))
    except Exception:
        print("none")
