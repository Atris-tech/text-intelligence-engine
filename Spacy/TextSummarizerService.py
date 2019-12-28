from pprint import pprint as print
from gensim.summarization import summarize
import requests

class TextSummarizerService:
    def summarizer(text):
        # text = requests.get('http://rare-technologies.com/the_big_lebowski_synopsis.txt').text
        x=summarize(str(text))
        return x