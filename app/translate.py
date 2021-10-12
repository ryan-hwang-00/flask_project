import json
import requests
from flask_babel import _
from app import app

# def translate(text, source_language, dest_language):
#     if 'MS_TRANSLATOR_KEY' not in app.config or \
#             not app.config['MS_TRANSLATOR_KEY']:
#         return _('Error: the translation service is not configured.')
#     auth = {
#         'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
#         'Ocp-Apim-Subscription-Region': 'westus2'}
#     r = requests.post(
#         'https://api.cognitive.microsofttranslator.com'
#         '/translate?api-version=3.0&from={}&to={}'.format(
#             source_language, dest_language), headers=auth, json=[{'Text': text}])
#     if r.status_code != 200:
#         return _('Error: the translation service failed.')
#     return r.json()[0]['translations'][0]['text']


import os
import sys
import urllib.request

def translate(text, source_language, dest_language):
    if not app.config['NAVER_CLIENT_ID'] or not app.config['NAVER_CLIENT_SECRET']:
        return _('Error: the translation service is not configured.')

    client_id = app.config['NAVER_CLIENT_ID'] # 개발자센터에서 발급받은 Client ID 값
    client_secret = app.config['NAVER_CLIENT_SECRET'] # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(text)
    data = f"source={source_language}&target={dest_language}&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    # print(rescode)
    if(rescode==200):
        response_body = response.read()
        return json.loads(response_body.decode('utf-8'))['message']['result']['translatedText']
    else:
        return _('Error: the translation service failed.')