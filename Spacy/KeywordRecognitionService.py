import yake
class KeywordRecognitionService:
    def keywordService(text):
        kw_extractor = yake.KeywordExtractor()
        keywords = kw_extractor.extract_keywords(text)
        keyword_priority_list=[]
        for kw in keywords:
            keyword_priority_list.append(kw)

        return keyword_priority_list