#!/usr/bin/python3
""" Top 10 subscribers """
import requests

def top_ten(subreddit):
    """Get top 10 hot posts from a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        req = requests.get(url, headers=headers, params={"limit": 10}, allow_redirects=False)
        
        if req.status_code == 200:
            data = req.json().get("data")
            if data and "children" in data:
                for child in data["children"]:
                    if "data" in child and "title" in child["data"]:
                        print(child["data"]["title"])
                    else:
                        print("Invalid post format: ", child)
            else:
                print("No data returned from Reddit.")
        else:
            print(None)
    except Exception as e:
        print(None)

