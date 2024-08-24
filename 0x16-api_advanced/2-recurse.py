#!/usr/bin/python3
""" 2-recurse.py """
import requests

def fetch_all_hot_posts(subreddit, hot_list=None, after=""):
    """
    Recursively retrieves and returns a list of titles for all hot posts in a subreddit.
    """
    # Initialize the list if it's the first call
    if hot_list is None:
        hot_list = []
    
    # Construct the API endpoint for hot posts
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Custom User-Agent to comply with Reddit API guidelines
    headers = {"User-Agent": "my-custom-agent:v2.0 (by /u/your_username)"}
    # Query parameters to specify the number of posts and the pagination cursor
    params = {"limit": 100, "after": after}

    try:
        # Send the GET request with headers and query parameters
        response = requests.get(api_url, headers=headers, params=params, allow_redirects=False)
        
        # If the request fails, return None
        if response.status_code != 200:
            return None
        
        # Extract post data from the JSON response
        data = response.json().get("data", {})
        posts = data.get("children", [])
        
        # Append the titles of the posts to the hot_list
        hot_list.extend(post.get("data", {}).get("title", "") for post in posts)
        
        # Get the "after" cursor for pagination
        after = data.get("after", None)
        
        # If there are more posts, recurse to retrieve them
        if after:
            return fetch_all_hot_posts(subreddit, hot_list, after)
        return hot_list
    
    except requests.RequestException:
        return None