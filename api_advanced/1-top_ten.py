#!/usr/bin/python3
"""
gets the top ten hot posts in a subreddit
"""
import requests


def top_ten(subreddit):
    """"gets the top ten hot posts in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if response.status_code != 200:
        print(None)
    else:
        json_response = response.json()
        for post in json_response[:10]:
            print(post.get('data').get('title')) 
#!/usr/bin/python3
""" module for function to return top 10 hot posts of a given subreddit """
import requests
import sys


def top_ten(subreddit):
    """ Returns: top ten post titles
        or None if queried subreddit is invalid """
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)
