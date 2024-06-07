#!/usr/bin/python3
"""Fetch the number of subscribers for a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: The number of subscribers or 0 if the subreddit is invalid.
    """
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:subscribers.fetcher:v1.0 (by /u/yourusername)'}
    
    try:
        response = requests.get(api_url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0
