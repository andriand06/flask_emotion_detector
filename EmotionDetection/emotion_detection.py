import requests
import json
def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { 'raw_document': { 'text': text_to_analyze } }
    response = requests.post(url=URL, json=myobj, headers=HEADERS)
    response_json = json.loads(response.text)
    if 'code' in response_json and response_json['code'] == '3':
        return { 
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }
    else:
        emotions = response_json['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        return { 
            "anger": anger_score, 
            "disgust": disgust_score, 
            "fear": fear_score, 
            "joy": joy_score, 
            "sadness": sadness_score, 
            "dominant_emotion": max(emotions, key=emotions.get) 
        }