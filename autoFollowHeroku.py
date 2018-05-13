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


def follow(keyword, a_cnt):
    follow_cnt = 0
	# 検索ワードと追加フォロー数をセットし検索実行
    search_results = api.search(q=keyword, count=a_cnt)
    for result in search_results:
        if follow_cnt <= a_cnt:
            try:
                screen_id = result.user._json["screen_name"]
                user_id = result.id
                api.create_friendship(screen_id)
                print("{0}をフォローしました。" .format(screen_id))
                time.sleep(2)
                follow_cnt += 1
            except tweepy.error.TweepError:
                print("フォローが失敗しました。")
                return follow_cnt



u_cnt = 0
f_cnt = 0
api, SCREEN_NAME = get_api()
keyword = "相互"
a_cnt = 8
print("成功")
