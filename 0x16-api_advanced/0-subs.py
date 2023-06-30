#!/usr/bin/python3
"""
Query the Reddit API and returns
number of subscribers in a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 302:
            # Redirect to search results indicates an invalid subreddit
            return 0
        else:
            # Other status codes indicate a failed request
            return 0
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
