# Reddit Comment Scraper and Giveaway Picker

This project provides a Python script to scrape comments from a Reddit thread and randomly pick a giveaway winner. It leverages the Reddit API via the praw library and outputs the data into a CSV file.

## Features

- Scrape all comments (including nested ones) from a specified Reddit thread.

- Save comments into a structured CSV file with the comment ID, author, and content.

- Randomly select a giveaway winner from the comments.

## Requirements

To run this script, ensure you have the following:

1. Python 3.6+

2. Reddit API credentials:

    - client_id

    - client_secret

    - user_agent

    You can apply for Reddit API access here by creating an app.

3.  Python Libraries:

    - praw
    
    - csv
    
    - os

Install dependencies using pip:

    `pip install praw`

## Setup

### 1. Environment Variables

Store your Reddit API credentials in environment variables for security:

- `REDDIT_CLIENT_ID`

- `REDDIT_CLIENT_SECRET`

- `REDDIT_USER_AGENT`

You can use a .env file or export them manually:

```
export REDDIT_CLIENT_ID='your_client_id'
export REDDIT_CLIENT_SECRET='your_client_secret'
export REDDIT_USER_AGENT='your_user_agent'
```
### 2. Running the Script

1. Clone this repository:

```
git clone https://github.com/rickknowlton/giveaway-buddy
cd giveaway-buddy
```
2. Run the script:

`python buddy.py`

3. Enter the Reddit thread URL when prompted.

4. The comments will be saved in `reddit_comments.csv`.

5. The script will randomly pick a giveaway winner from the collected comments.

### 3. Output

- CSV File: Contains all the comments from the thread.

- Winner: Printed in the terminal with the comment and author details.

## Example

Suppose you run the script and provide a thread URL. The script will scrape all comments and save them to a CSV file like this:

| Comment ID  | Author | Comment |
| :-------------: | :-------------: | :------------- |
| xyz123     | username1     |Witty Comment!             |
| xyz567     | username2     |Another witty comment!     |

It will then randomly pick a winner, e.g., "username2: Another witty comment!".

## Contributing

Feel free to fork this repository and submit pull requests for improvements or new features.

## License

This project is open-source and available under the MIT License.