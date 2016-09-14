#!/Users/Sandeep/miniconda2/envs/ML
import json
import requests
import tweepy
from stream import StreamListener

SECRETS_FILE = "secrets.json"

def main():
	api = authorize()
	stream = tweepy.Stream(auth = api.auth, listener=StreamListener())
	for tweet in stream.filter(track=['soccer', 'Soccer', 'SOCCER']):
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