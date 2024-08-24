#!/usr/bin/python3
""" 1-top_ten.py """
import requests

def fetch_top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.
    If the subreddit is invalid, it prints "None".
    """
    # Construct the Reddit API URL for the hot posts
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Define custom User-Agent for the request
    headers = {"User-Agent": "my-custom-agent:v2.0 (by /u/your_username)"}
    # Set query parameters to limit the number of posts retrieved
    params = {"limit": 10}
    
    try:
        # Send the GET request with specified headers and params
        response = requests.get(api_url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code != 200:
            print("None")
            return
        
        # Parse the JSON data to get the list of hot posts
        posts = response.json().get("data", {}).get("children", [])
        
        # Extract and print the titles of the posts
        for post in posts:
            print(post.get("data", {}).get("title", ""))
    
    except requests.RequestException:
        print("None")

# Example usage
if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit: ")
    fetch_top_ten(subreddit_name)
