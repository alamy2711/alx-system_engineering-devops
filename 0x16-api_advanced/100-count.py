#!/usr/bin/python3
""" 100-count.py """
from collections import defaultdict
import requests

def word_count_in_subreddit(subreddit, word_list, titles=[], first_call=True, after=None):
    """
    Recursively fetches hot post titles from a subreddit and counts the occurrences
    of specified words, then prints the word counts.
    """
    # Build the Reddit API endpoint URL
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Custom User-Agent to follow Reddit API rules
    headers = {"User-Agent": "custom-agent:v3.0 (by /u/your_username)"}
    # Parameters for limiting the number of posts and pagination
    params = {"limit": 100, "after": after}

    try:
        # Make the GET request to the API
        response = requests.get(api_url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code == 200:
            # Extract the post data
            data = response.json().get("data", {})
            after = data.get("after")
            posts = data.get("children", [])
            
            # Append titles to the list
            titles += [post.get("data", {}).get("title", "") for post in posts]
            
            # If more pages are available, recurse with the updated cursor
            if after:
                word_count_in_subreddit(subreddit, word_list, titles, first_call=False, after=after)
            
            # On the initial call, process the titles and count words
            if first_call:
                word_counts = defaultdict(int)
                combined_titles = " ".join(titles).lower().split()
                
                # Count occurrences of each word in word_list
                for word in word_list:
                    word_lower = word.lower()
                    word_counts[word_lower] += combined_titles.count(word_lower)
                
                # Filter out words that have no occurrences
                sorted_word_counts = sorted(
                    [(word, count) for word, count in word_counts.items() if count > 0],
                    key=lambda x: (-x[1], x[0])
                )
                
                # Print the results
                for word, count in sorted_word_counts:
                    print(f"{word}: {count}")
    
    except requests.RequestException:
        return