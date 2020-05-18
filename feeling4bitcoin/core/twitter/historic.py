import tweepy

from core.twitter.credential import Credential
from data.tweet_model import TweetModel


class Historic:

    def __init__(self):
        self.credential = Credential()

    def start(self):

        print("start")
        model = TweetModel()

        api = self.credential.api()
        tweets = tweepy.Cursor(api.search,
                               q='bitcoin OR satoshi OR BTC',
                               lang='en').items(50000000)

        for tweet in tweets:
            data = {'coordinates': tweet.coordinates, 'text': tweet.text, 'created_at': tweet.created_at}
            print(data)
            model.insert(data)


Historic().start()
