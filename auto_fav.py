from requests_oauthlib import OAuth1Session
import json
import random
import datetime
import tweepy
import os
import time
from urllib import request

def get_api():
    keys = dict(
        screen_name = 'sqdope',
        CK = os.environ["CK"],       # Consumer Key
        CS = os.environ["CS"],         # Consumer Secret
        AT = os.environ["AT"], # Access Token
        AS = os.environ["AS"]         # Accesss Token Secert
    )

    SCREEN_NAME = keys['screen_name']
    CONSUMER_KEY = keys['CK']
    CONSUMER_SECRET = keys['CS']
    ACCESS_TOKEN = keys['AT']
    ACCESS_TOKEN_SECRET = keys['AS']

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api, SCREEN_NAME


api, SCREEN_NAME = get_api()
tws = api.home_timeline()
for v in tws:
    id = v.id
    api.create_favorite(id)
    time.sleep(1)
