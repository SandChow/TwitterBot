#!/Users/Sandeep/miniconda2/envs/ML
import json
import requests
import tweepy

def main():
    # Twitter API setup
    with open(SECRETS_FILE) as f:
        secrets = json.load(f)
    auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_secret'])
    api = tweepy.API(auth)