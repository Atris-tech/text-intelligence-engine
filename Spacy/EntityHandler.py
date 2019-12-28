
from .EntityRecognizationService import EntityRecognization

entityObj=EntityRecognization()


class EntityHandler:
    def entity(self,text):
        entity_dict={}
        entity_list=[]
        error_list=['match not found']
        entity_list=entityObj.entityRecog(text)
        if entity_list:
            resp = {

            "status": "success",
            "data": [entity_dict,entity_list]
        }
            return resp
        # else:
        #     resp={
        #         "status": "error",
        #         "data": [entity_dict,error_list]
        #
        #     }


