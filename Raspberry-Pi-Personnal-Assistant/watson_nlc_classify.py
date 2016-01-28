#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Sends Classify requests to a trained and available IBM Watson Natural Language Classifier.
#Requires valid credentials in the bluemix.py file.
#
#Usage: watson_nlc_classify.py <Classifier_ID> "<question>"
#   where <Classifier_ID> is a trained and available Classifier (see watson_nlc_create.py and watson_nlc_list.py)
#   and "<question>" represents the text to be classified

import requests
import json
import sys
import urllib

import bluemix

if len(sys.argv) != 3:
	print 'watson_nlc_classify.py <Classifier_ID> "<question>"'
	sys.exit(2)


#Construct the URL based on the parameters provided
url = bluemix.url  + '/' + sys.argv[1] + '/classify?text=' + urllib.quote_plus(sys.argv[2])

#Send a request to our trained classifier
try:
	r = requests.get(url, auth=(bluemix.user, bluemix.pwd))
	print r.status_code
	try:
        #Displays the returned Classes and confidences
		data = json.loads(r.text)
                print "Question:   ", data['text']
                print "Top Class:  ", data['top_class']
		for response in data['classes']:
                	print "\nClass:      ", response['class_name']
                	print "Confidence: ", response['confidence']
	except:
		print r.text
except Exception, e:
	print e



