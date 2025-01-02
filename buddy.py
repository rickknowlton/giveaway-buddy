import praw

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id="client_id",
    client_secret="client_secret",
    user_agent="user_agent"
)

# Fetch the thread
submission = reddit.submission(url="https://www.reddit.com/r/subreddit/comments/post_id/")

# Retrieve comments
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    print(comment.body)
