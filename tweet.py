from requests_oauthlib import OAuth1Session
import json
import random
import datetime
import os

twitter = OAuth1Session(os.environ["CK"],  os.environ["CS"], os.environ["AT"], os.environ["AS"])
#heroku config:set CONSUMER_KEY=*** CONSUMER_SECRET=*** ACCESS_TOKEN_KEY=*** ACCESS_TOKEN_SECRET=***

# タイムライン取得用のURL
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

# とくにパラメータは無い
params = {}


# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
tweets = ["当たり前だよなあ","お、そうだな","焼いてかない？"]   #ここにツイートする内容を入れる
randomtweet = tweets[random.randrange(len(tweets))]
timestamp = datetime.datetime.today()
timestamp = str(timestamp.strftime("%Y/%m/%d %H:%M"))   #タイムスタンプを用意

params = {"status": randomtweet + " " + timestamp}


# OAuth認証で POST method で投稿

req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
