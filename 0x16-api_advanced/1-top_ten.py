#!/usr/bin/python3
"""Get top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Top 10 hot posts"""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'gritnec'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print(None, response.status_code)


top_ten('programming')
