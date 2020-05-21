import GetOldTweets3 as got;

from core.twitter.credential import Credential
from data.tweet_model import TweetModel
from datetime import datetime
from datetime import timedelta
import time


class Historic:

    def __init__(self):
        self.credential = Credential()

    def start(self, data, fim):

        if data == fim:
            return

        print("start")
        model = TweetModel()

        inicio = data
        data += timedelta(days=1)

        print("buscando tweets do dia " + inicio.strftime("%Y-%m-%d") + " até " + data.strftime("%Y-%m-%d"))

        try:
            criteria = got.manager.TweetCriteria() \
                .setLang('en') \
                .setQuerySearch('bitcoin') \
                .setMaxTweets(1000) \
                .setSince(inicio.strftime("%Y-%m-%d")).setUntil(data.strftime("%Y-%m-%d"))

            tweets = got.manager.TweetManager.getTweets(criteria)

            for tweet in tweets:
                json = {'id': tweet.id, 'text': tweet.text, 'created_at': tweet.date}
                print(json)
                model.insert(json)
        except:
            print("Falha na busca de tweets")

        time.sleep(30)
        self.start(data, fim)


Historic().start(datetime(2019, 8, 19), datetime(2020, 1, 1))
