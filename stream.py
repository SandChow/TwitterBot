import tweepy
import re
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
    	if not re.search('^RT', status.text):
    		print status.text