#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Makes a request to the IBM Watson Text to Speech API, saves the result as a Wave file
#and plays the file using mplayer

import requests
import os
from os.path import join, dirname

        
user = "<Replace with your Bluemix Service username>"
pwd = "<Replace with your Bluemix Service password>"

#French language example
#text='Bonjour, comment ca va?'
#params = {'text': text, 'voice': 'fr-FR_ReneeVoice', 'accept': 'audio/wav'}

text='Hello, how are you?'
params = {'text': text, 'voice': 'en-US_MichaelVoice', 'accept': 'audio/wav'}

headers = {'content-type': 'audio/wav'}

url='https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize'
r = requests.request(method='POST', url=url, headers=headers, params=params,
                            stream=True, auth=(user, pwd))

if r.status_code == 200:
    #Write the file to disk
    filename='output.wav'
    with open(filename, 'wb') as audio_file:
        audio_file.write(r.content)
    print join(dirname(__file__), filename)
    #Play the audio file with your favorite player
    os.system('/usr/bin/mplayer ' + join(dirname(__file__), filename))
    #Delete the file
    os.remove(filename)
else:
    print r.status_code
    print r.headers
    print r.text   


