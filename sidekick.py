import praw
import re

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    user_agent="USER_AGENT",
)

# Function to extract numbers within a range from comments
def extract_numbers_in_range(comments, lower_bound, upper_bound):
    numbers = set()  # Use a set to avoid duplicates
    for comment in comments:
        # Extract all numbers in the comment
        found_numbers = re.findall(r'\b\d+\b', comment.body)
        for number in found_numbers:
            num = int(number)
            if lower_bound <= num <= upper_bound:
                numbers.add(num)
    return numbers

# Main function
def main():
    url = "https://www.reddit.com/r/subreddit/comments/thread_id/"
    lower_bound = 2000
    upper_bound = 2500

    # Fetch the thread and comments
    submission = reddit.submission(url=url)
    submission.comments.replace_more(limit=None) 
    all_comments = submission.comments.list()

    # Extract picked numbers within bounds
    picked_numbers = extract_numbers_in_range(all_comments, lower_bound, upper_bound)

    # Derive remaining numbers
    full_range = set(range(lower_bound, upper_bound + 1))
    remaining_numbers = full_range - picked_numbers

    # Write picked numbers to a file
    with open("picked_numbers.txt", "w") as f:
        for number in sorted(picked_numbers):
            f.write(f"{number}\n")
    print("Picked numbers saved to picked_numbers.txt")

    # Write remaining numbers to a file
    with open("remaining_numbers.txt", "w") as f:
        for number in sorted(remaining_numbers):
            f.write(f"{number}\n")
    print("Remaining numbers saved to remaining_numbers.txt")

if __name__ == "__main__":
    main()