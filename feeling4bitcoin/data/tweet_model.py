from pymongo import MongoClient


class TweetModel:

    def __init__(self):
        self.cliente = MongoClient('mongodb://localhost:27017/')
        self.banco = self.cliente['feeling4bitcoin']
        self.album = self.banco['tweet']

    def insert(self, tweet):
        self.album.insert_one(tweet)

