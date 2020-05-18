import tweepy


class Credential:

    def __init__(self):
        self.consumer_key = 'J4hDogeC12Oc4ht7PIaWqgusn'
        self.consumer_secret = 'wdBWEhbDLGWJVzwrTHMvmbuujDN6acndj01YryJ0paS2DYDjgS'
        self.access_token = '1042595799639777285-MhPBV7rsBVyxl0voIskuNY3bri1Vzy'
        self.access_token_secret = 'XHpPHRwXoC7vT6U0514GbTh6lwOxCqG4KXIqLF7sG8GwD'

    def api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth)
