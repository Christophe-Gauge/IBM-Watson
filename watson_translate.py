#!/usr/bin/env python2
# -*- coding: utf-8-*-


import requests

user = "<Replace with your Bluemix Service username>"
pwd = "<Replace with your Bluemix Service password>"

headers = {'content-type': 'plain/text'}
#text='Hola, cómo estás?'
text='Hello, how are you?'

data = {'text': text, 'source': 'en',
        'target': 'fr'}

url='https://gateway.watsonplatform.net/language-translation/api/v2/translate'
r = requests.request(method='POST', url=url, headers=headers, data=data,
                            stream=True, auth=(user, pwd))

if r.status_code == 200:
    print r.text
else:
    print r.status_code
    print r.headers
    print r.text   

