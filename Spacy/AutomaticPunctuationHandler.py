from .AutomaticPunctuationService import AutomaticPunctuationService

punctuationObj = AutomaticPunctuationService()
class AutomaticPunctuationHandler:
    def punctuationHandler(text):
        segments_list=[]
        segments_list=punctuationObj.punctuationService(text=text)
        resp = {
            "status": "success",
            "data": segments_list
        }
        return resp