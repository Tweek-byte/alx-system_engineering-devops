#!/usr/bin/python3
""" Module for storing the count_words function. """
import re
import requests

def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Prints the count of the given words present in the title of the
    subreddit's hottest articles.
    """
    if word_count is None:
        word_count = {}

    headers = {'User-Agent': 'Mozilla/5.0'}

    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return

    data = r.json().get('data')
    if not data:
        return

    children = data.get('children', [])
    for child in children:
        title = child['data']['title'].lower()
        for word in word_list:
            # Word matching with boundary to avoid matching parts of words
            # and ignoring word separators like ".", "!", or "_"
            match_count = len(re.findall(rf'\b{re.escape(word.lower())}\b', title))
            if match_count > 0:
                word_count[word] = word_count.get(word, 0) + match_count

    after = data.get('after')
    if after:
        count_words(subreddit, word_list, word_count, after)
    else:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_words:
            print(f'{word.lower()}: {count}')
