from .TextSummarizerService import TextSummarizerService
summarizerObj=TextSummarizerService

class TextSummarizerHandler:
    def summarizerHandler(text):
        str_text=summarizerObj.summarizer(text)

        resp = {
            "status": "success",
            "data": str_text
        }
        return resp