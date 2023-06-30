#!/usr/bin/python3
"""
Query the Reddit API and returns
the top ten hot posts of a subreddit.
"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts[:10]:
                title = post['data']['title']
                print(title)
        elif response.status_code == 302:
            # Redirect to search results indicates an invalid subreddit
            print("None")
        else:
            # Other status codes indicate a failed request
            print("None")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
