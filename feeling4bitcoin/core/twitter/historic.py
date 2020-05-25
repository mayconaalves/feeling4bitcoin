import time
import re

from datetime import datetime
from datetime import timedelta

import GetOldTweets3 as got;
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from core.twitter.credential import Credential
from data.tweet_model import TweetModel


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
            time.sleep(30)

            criteria = got.manager.TweetCriteria() \
                .setLang('en') \
                .setQuerySearch('bitcoin') \
                .setMaxTweets(2000) \
                .setSince(inicio.strftime("%Y-%m-%d")).setUntil(data.strftime("%Y-%m-%d"))

            tweets = got.manager.TweetManager.getTweets(criteria)

            for tweet in tweets:
                analyser = SentimentIntensityAnalyzer()

                text_clean = clean(tweet.text)
                score = analyser.polarity_scores(text_clean)

                json_data = {'id': tweet.id,
                             'text': text_clean,
                             'created_at': tweet.date,
                             'retweets': tweet.retweets,
                             'neg': score['neg'],
                             'neu': score['neu'],
                             'pos': score['pos'],
                             'compound': score['compound']}
                print(json_data)
                model.insert(json_data)

            self.start(data, fim)
        except:
            print("Falha na busca de tweets")
            self.start(inicio, fim)


def clean(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r'@[\w]*', "", text)
    text = re.sub(r'RT @[\w]*', "", text)
    text = re.sub(r'[^a-zA-Z#!:)(=)]', ' ', text)
    text = re.sub(' +', ' ', text)

    return text


Historic().start(datetime(2020, 4, 12), datetime(2020, 5, 1))
