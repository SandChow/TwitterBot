#!/Users/Sandeep/miniconda2/envs/ML
import json
import requests
import tweepy
from stream import MyStreamListener

SECRETS_FILE = "secrets.json"

def main():
	api = authorize()
	myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
	for tweet in myStream.filter(track=['soccer'], locations=[-122.75,36.8,-121.75,37.8,-74,40,-73,41]):
		if not tweet['retweeted'] and 'RT @' not in tweet['text']:
			if 'soccer' in tweet['text']:
				print tweet

def authorize():
    # Twitter API setup
    with open(SECRETS_FILE) as f:
        secrets = json.load(f)
    auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_secret'])
    api = tweepy.API(auth)
    return api

if __name__ =="__main__":
	main()