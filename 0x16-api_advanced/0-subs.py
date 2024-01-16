#!/usr/bin/python3
"""Fetch subreddit subs"""
import requests


def number_of_subscribers(subreddit):
    """Fetch reddit subs"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'gritnec/1.0 (by /u/johngaitho)'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        subscribers_count = data['data']['subscribers']
        return subscribers_count
    except KeyError:
        return 0
