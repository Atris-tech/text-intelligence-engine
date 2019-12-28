from watson_developer_cloud import *

def diar(wav_file):
    # output_json = wav_file.replace('.wav', '.json')

    speech_to_text = SpeechToTextV1(
        iam_apikey = 'b-PTdCl8YJtxjnx0ZTpoHp_4ynUJJYTGgRRmJWP-GzCv',
        url='https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/d3a9f964-d274-4151-bf35-e020d3c3e0af',
    )

    # speech_to_text = NaturalLanguageUnderstandingV1(username = 'Adarsh Gupta', password = 'Pappu$1960', version = '2')
    speech_to_text.set_default_headers({'x-watson-learning-opt-out': "true"})
    #
    # print(json.dumps(speech_to_text.models(), indent=2))

    # print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

    with open(wav_file, 'rb') as audio:
        result = speech_to_text.recognize(audio, content_type='audio/wav', timestamps=True,
            word_confidence=True, speaker_labels=True)
    return result
        # with open(output_json, 'w') as f:
        #     json.dump(result, f, ensure_ascii=False)
        # print(result)

