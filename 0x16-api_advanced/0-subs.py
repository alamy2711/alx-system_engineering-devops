#!/usr/bin/python3
""" 0-subs.py """
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, it returns 0.
    """
    # Create the URL for the subreddit's about.json endpoint
    endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set a custom User-Agent to comply with Reddit's API guidelines
    headers = {"User-Agent": "custom-script:v1.0 (by /u/your_username)"}
    
    try:
        # Make the GET request with redirects disabled
        response = requests.get(endpoint, headers=headers, allow_redirects=False)
        
        # If the status code isn't 200, return 0 (likely an invalid subreddit)
        if response.status_code != 200:
            return 0
        
        # Attempt to extract the subscriber count from the response JSON
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    
    except requests.exceptions.RequestException:
        # Return 0 if any request-related error occurs
        return 0
