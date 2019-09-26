from requests_oauthlib import OAuth1Session
import json
import random
import datetime
import tweepy
import time
import os
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

def unfollow(api, followers, friends):
    unfollow_cnt = 0
    for f in friends:
        if f not in followers:
            if unfollow_cnt <= 100:
               api.destroy_friendship(f)
               print("{0}のフォローを解除しました。".format(api.get_user(f).screen_name))
               time.sleep(2)
               unfollow_cnt += 1
            else:
                print('一度に解除可能な人数に達したため処理を中断します。')
                break
    for f in followers:
        if f not in friends:
            try:
                api.create_friendship(f)
                print("{0}をフォローしました。".format(api.get_user(f).screen_name))
                time.sleep(2)
            except tweepy.error.TweepError:
            	print("フォローが失敗しました。")
    return unfollow_cnt

if __name__ == "__main__":
    u_cnt = 0
    f_cnt = 0
    api, SCREEN_NAME = get_api()
    followers = api.followers_ids(SCREEN_NAME)
    friends = api.friends_ids(SCREEN_NAME)
    u_cnt = unfollow(api, followers, friends)
