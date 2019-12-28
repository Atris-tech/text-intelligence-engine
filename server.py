from fastapi import FastAPI, File, UploadFile,HTTPException
from Spacy.EntityHandler import EntityHandler
from Spacy.KeywordHandler import KeywordHandler
from Spacy.AutomaticPunctuationHandler import AutomaticPunctuationHandler
from Spacy.TextSummarizerHandler import TextSummarizerHandler
from Spacy.SentimentHandler import SentimentHandler
import diar
import uuid
import os
from watson_developer_cloud import *


app = FastAPI()

speech_to_text = SpeechToTextV1(
        iam_apikey = 'b-PTdCl8YJtxjnx0ZTpoHp_4ynUJJYTGgRRmJWP-GzCv',
        url='https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/d3a9f964-d274-4151-bf35-e020d3c3e0af',
    )

entityHandler=EntityHandler()

keywordHandler=KeywordHandler()



@app.post("/entityrecog/")
def get_entity(text:str):
    print(text)
    output=entityHandler.entity(text)
    return output

@app.post("/keywordrecog/")
def get_keyword(text: str):
    output=keywordHandler.keyword(text)
    if output["status"] == "error":
        raise HTTPException(status_code=400, detail="Bad Request")
    return output

@app.get("/autopunctuation/{text}")
def get_segments(text:str):
    output=AutomaticPunctuationHandler.punctuationHandler(text)
    return output

@app.post("/textsummarizer/")
def get_summarizer(text:str):
    output=TextSummarizerHandler.summarizerHandler(text)
    return output

@app.post('/sentiment/')
def get_sentiments(text:str):
    output=SentimentHandler.sentimentAnalysis(text)
    return output

@app.post("/diarisation/")
async def get_diarisation(file: UploadFile = File(...)):
    audio = await file.read()
    uniqueFileName = "audio_dir/" + str(uuid.uuid4()) + ".wav"
    with open(uniqueFileName, 'wb') as f:
        f.write(audio)
    with open(uniqueFileName, 'rb') as audio:
        result = speech_to_text.recognize(audio, content_type='audio/wav', timestamps=True,
                                          word_confidence=True, speaker_labels=True)

    return result