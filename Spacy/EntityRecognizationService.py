import re

import spacy
class EntityRecognization:
    def entityRecog(self, text):

        nlp = spacy.load("en_core_web_sm")
        print(nlp)
        doc = nlp(text)
        print(doc)

        # entity_text = []
        # entity_label=[]
        # for entity in doc.ents:
        #     dic[entity.label_]=entity.text
        #
        #     # entity_text.append(entity.text)
        #     # entity_label.append(entity.label_)
        PERSON = []
        NORP = []
        FAC = []
        ORG = []
        GPE = []
        LOC = []
        PRODUCT = []
        EVENT = []
        WORK_OF_ART = []
        LAW = []
        LANGUAGE = []
        DATE = []
        TIME = []
        PERCENT = []
        MONEY = []
        QUANTITY = []
        ORDINAL = []
        CARDINAL = []

        for entity in doc.ents:

            if str(entity.label_) == "PERSON":
                PERSON.append(entity.text)

            elif str(entity.label_) == "NORP":
                NORP.append(entity.text)

            elif str(entity.label_) == "FAC":
                FAC.append(entity.text)

            elif str(entity.label_) == "ORG":
                ORG.append(entity.text)

            elif str(entity.label_) == "GPE":
                GPE.append(entity.text)

            elif str(entity.label_) == "LOC":
                LOC.append(entity.text)

            elif str(entity.label_) == "PRODUCT":
                PRODUCT.append(entity.text)

            elif str(entity.label_) == "EVENT":
                EVENT.append(entity.text)

            elif str(entity.label_) == "WORK_OF_ART":
                WORK_OF_ART.append(entity.text)

            elif str(entity.label_) == "LAW":
                LAW.append(entity.text)

            elif str(entity.label_) == "LANGUAGE":
                LANGUAGE.append(entity.text)

            elif str(entity.label_) == "DATE":
                DATE.append(entity.text)

            elif str(entity.label_) == "TIME":
                TIME.append(entity.text)

            elif str(entity.label_) == "PERCENT":
                PERCENT.append(entity.text)

            elif str(entity.label_) == "MONEY":
                MONEY.append(entity.text)

            elif str(entity.label_) == "QUANTITY":
                QUANTITY.append(entity.text)

            elif str(entity.label_) == "ORDINAL":
                PERSON.append(entity.text)

            elif str(entity.label_) == "CARDINAL":
                CARDINAL.append(entity.text)


        labels = {
            "PERSON": PERSON,
            "NORP": NORP,
            "FAC"	:  FAC,
            "ORG"	 :  ORG,
            "GPE"	 : GPE,
            "LOC"	 :  LOC,
            "PRODUCT" :	PRODUCT ,
            "EVENT" : EVENT,
            "WORK_OF_ART" : WORK_OF_ART,
            "LAW" : LAW,
            "LANGUAGE" : LANGUAGE,
            "DATE" : DATE,
            "TIME" : TIME,
            "PERCENT" : PERCENT,
            "MONEY" : MONEY,
            "QUANTITY" : QUANTITY,
            "ORDINAL ": ORDINAL,
            "CARDINAL" : CARDINAL,
        }
        empty_keys = [k for k ,v in labels.items() if not v]
        for k in empty_keys:
            del labels[k]
        print(labels)
        dict = {}
        list = []
        inner_list=[]
        # error="no match found"
        for entity in doc.ents:

                match = re.search(str(entity), text)
                if match:
                    dict["start"] = match.start()
                    dict["end"] = match.end()
                    dict["tag"] = entity.label_
                    dict["text"] = entity.text
                    list.append(dict)
                    # print('%d,%d' % (match.start()-1, match.end()-1))
                    # print(list)
                # else:
                #     return list.append("match not found")
#labels is a dictionary
        return list

