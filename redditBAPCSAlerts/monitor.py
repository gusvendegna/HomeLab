import os
import praw
import requests

reddit = praw.Reddit(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    user_agent=os.environ["USER_AGENT"]
)

subreddit = reddit.subreddit("buildapcsales")

keywords = ["ssd", "hdd"]

# Replace with your Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/..."


def send_discord_message(content):
    data = {"content": content}
    requests.post(WEBHOOK_URL, json=data)


for post in subreddit.stream.submissions(skip_existing=True):
    title = post.title.lower()
    if any(keyword in title for keyword in keywords):
        message = f"New post: {post.title} (https://www.reddit.com{post.permalink})"
        print(message)
        send_discord_message(message)
