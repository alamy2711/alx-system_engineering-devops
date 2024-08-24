#!/usr/bin/python3
""" 0-subs.py """
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    If the subreddit is invalid or does not exist, returns 0.
    """
    # Construct the API URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set the custom User-Agent header
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/your_username)"}

    try:
        # Make the GET request with redirect disabled
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse and return the number of subscribers
            return response.json().get('data', {}).get('subscribers', 0)
        else:
            # If the subreddit is invalid or any other error occurs, return 0
            return 0
    except requests.RequestException:
        # If any request-related error occurs, return 0
        return 0
