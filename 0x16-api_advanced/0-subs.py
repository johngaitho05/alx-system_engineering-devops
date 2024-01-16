#!/usr/bin/python3
"""Fetch subreddit subs"""
import requests


def number_of_subscribers(subreddit):
    """Fetch reddit subs"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'gritnec/1.0 (by /u/johngaitho)'}
    response = requests.get(url, headers=headers)
    data = response.json() or {}
    return data.get('data', {}).get('subscribers', 0)
