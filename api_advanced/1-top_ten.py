#!/usr/bin/python3
""""Doc"""
import requests


def top_ten(subreddit):
    """"Doc"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if response.status_code != 200:
        print(None)
    else:
        json_response = response.json()
        for post in json_response[:10]:
            print(post.get('data').get('title')) 
