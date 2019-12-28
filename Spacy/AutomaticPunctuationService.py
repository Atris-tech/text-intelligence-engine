from deepcorrect import DeepCorrect
import os
class AutomaticPunctuationService:

    def punctuationService(self, text):
        model_path = str(os.path.abspath("punc_models")) + "/deeppunct_params_en"
        checkpoints = str(os.path.abspath("checkpoint")) + "/deeppunct_checkpoint_google_news"
        print(model_path)
        print(checkpoints)
        corrector = DeepCorrect(model_path, checkpoints)
        segments_list=[]
        segments_list=corrector.correct(text)
        return segments_list


