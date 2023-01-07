# Importing Tweepy and time
import tweepy
import time

# Please replace with your Credentials
api_key = "Your API Key"
api_secret = "Your API Secret"
bearer_token = r"Your Bearer Token"
access_token = "Your Access Token"
access_token_secret = "Your Access Token Secret"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret,
                       access_token, access_token_secret)

# Connecting to Twitter API
auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Please replace it with your choice of reply
message = "Your Reply Text"

# main code for RT, like and reply 
class MyStream(tweepy.StreamingClient):

    def on_tweet(self, tweet):

        try:
            print("Tweet/Reply found")
            client.retweet(tweet.id)
            client.like(tweet.id)
            client.create_tweet(
                in_reply_to_tweet_id=tweet.id, text=message)
            print("task completed")
            # Delay (so the bot doesn't search for new tweets a bucn of time each second)
            time.sleep(60)

        except Exception as error:
            print('time for power nap')
            print(error)
            time.sleep(3600)


stream = MyStream(bearer_token=bearer_token)

# Set Stream Rules
stream.add_rules(tweepy.StreamRule(
    "(YOUR STREAM RULES)"), dry_run=False)

# Start Stream
print("Starting stream...")
stream.filter()
