import flair
from flair.data import Sentence
flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
class SentimentHandler:
    def sentimentAnalysis(text):
        s = flair.data.Sentence(text)
        flair_sentiment.predict(s)
        total_sentiment = s.labels
        return total_sentiment



        # sentence = "bad is this world worst ever world which kills each other"
        # s = flair.data.Sentence(sentence)
        # flair_sentiment.predict(s)
        # total_sentiment = s.labels
        # total_sentiment

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                