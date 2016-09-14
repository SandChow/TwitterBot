import tweepy
import re
#override tweepy.StreamListener to add logic to on_status
class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
    	if not re.search('^RT', status.text):
    		if 'soccer' in status.text:
				print status.text