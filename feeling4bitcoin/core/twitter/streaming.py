import tweepy
from tweepy.streaming import StreamListener

from core.twitter.credential import Credential
from data.tweet_model import TweetModel


class Listener(StreamListener):
    def __init__(self):
        super(Listener, self).__init__()
        self.model = TweetModel()

    def on_status(self, tweet):

        data = {'text': tweet.text, 'created_at': tweet.created_at}
        print(data)
        self.model.insert(data)

    def on_error(self, status_code):
        print(status_code)
        return False


class Streaming:

    def __init__(self):
        self.credential = Credential()

    def start(self):
        api = self.credential.api()
        stream = tweepy.Stream(auth=api.auth, listener=Listener())
        stream.filter(track=['bitcoin', 'satoshi', 'BTC'])

        try:
            print('Start streaming.')
            stream.sample(languages=['en'])
        except KeyboardInterrupt as e:
            print("Stopped.")
        finally:
            print('Done.')
            stream.disconnect()


Streaming().start()
