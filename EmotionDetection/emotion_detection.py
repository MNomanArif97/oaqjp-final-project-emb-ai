import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)
    
    # Extracting emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Finding the dominant emotion
    emotion_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
    dominant_emotion_index = emotion_list.index(max(emotion_list))
    emotion_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    dominant_emotion = emotion_keys[dominant_emotion_index]
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }