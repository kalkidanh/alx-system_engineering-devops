#!/usr/bin/python3
"""Function that queries the reddit API and returns the number of
subscribers for a given sub-reddit."""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscriber for a subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'chrome 51.0.2704.106'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        number = response.json()
        return number.get('data').get('subscribers')
    else:
        return 0
