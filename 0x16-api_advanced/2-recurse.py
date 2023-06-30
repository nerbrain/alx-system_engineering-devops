#!/usr/bin/python3
"""
queries Reddit API and returns a list containing
titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            # Check if there is a next page
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list=hot_list)
            else:
                return hot_list
        elif response.status_code == 302:
            # Redirect to search results indicates an invalid subreddit
            return None
        else:
            # Other status codes indicate a failed request
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
