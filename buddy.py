import praw
import pandas as pd
import random

# Configure Reddit API client
reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    user_agent="USER_AGENT",
)

# Function to scrape comments from a thread
def scrape_reddit_comments(thread_url, output_csv="comments.csv"):
    submission = reddit.submission(url=thread_url)
    submission.comments.replace_more(limit=None)
    comments = []
    for comment in submission.comments.list():
        comments.append({
            "author": comment.author.name if comment.author else "Deleted",
            "comment": comment.body
        })
    
    df = pd.DataFrame(comments)
    df.to_csv(output_csv, index=False)
    print(f"Comments exported to {output_csv}")
    return df

# Function to pick a random winner
def pick_winner(csv_file):
    df = pd.read_csv(csv_file)
    winner = df.sample(1).iloc[0]
    print(f"The winner is: {winner['author']} with the comment: {winner['comment']}")
    return winner

# Example Usage
thread_url = "https://www.reddit.com/r/subreddit/comments/thread_id/"
csv_file = "comments.csv"

comments_df = scrape_reddit_comments(thread_url, csv_file)
pick_winner(csv_file)
