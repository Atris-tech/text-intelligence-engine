from Spacy.KeywordRecognitionService import KeywordRecognitionService

keywordObj=KeywordRecognitionService()

class KeywordHandler:
    def keyword(self,text):
        keyword_priority_list=[]
        keyword_priority_list=KeywordRecognitionService.keywordService(text)
        resp = {
            "status": "success",
            "data": keyword_priority_list
        }
        return resp
