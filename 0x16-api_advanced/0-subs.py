#!/usr/bin/python3
"""
How many subs?
"""
import requests


def number_of_subscribers(subreddit):
    """
    Count subreddit subscribers
    """
    api_header = {
        'User-Agent': 'Mozilla/5.0'
    }
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    api_res = requests.get(api_url, headers=api_header, allow_redirects=False)
    if api_res.status_code != 200:
        return 0
    api_json = api_res.json()
    return api_json['data']['subscribers']
