import tweepy
from django.conf import settings


class TwitterAPI:
    def __init__(self):
        self.consumerKey = settings.API_KEY
        self.consumerSecret = settings.API_KEY_SECRET
        self.accessToken = settings.ACCESS_TOKEN
        self.accessTokenSecret = settings.ACCESS_TOKEN_SECRET
        self.is_authenticated = False

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
        auth.set_access_token(self.accessToken, self.accessTokenSecret)
        self.api = tweepy.API(auth)
        self.is_authenticated = True

    def tweet(self, tweet):
        if self.is_authenticated:
            self.api.update_status(tweet)
        else:
            print("Authenticate first")
