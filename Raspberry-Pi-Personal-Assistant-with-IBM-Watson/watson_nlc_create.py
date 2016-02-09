#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Creates a new IBM Watson Natural Language Classifier based on CSV Data provided.
#Retrieves Classifier status until training is done. Requires valid credentials in the bluemix.py file.

import json
import requests
import sys
import time

import bluemix

#Set the desired language, Classifier name, and the location of the training CSV file
data = {
    'training_metadata': ('{"language":"en","name":"My Personal Assistant Classifier"}'),
}

files = {
    'training_data': ('training.csv', open('training.csv').read()),
}

#Send the request to create the classifier
try:
	r = requests.post(bluemix.url, files=files, data=data, auth=(bluemix.user, bluemix.pwd))
	print r.status_code
	try:
		data = json.loads(r.text)
		newClassifier = data['classifier_id']
		print "New Classifier was created with ID: %s" % newClassifier
	except:
		print r.text
		sys.exit(1)
except Exception, e:
	print e
	sys.exit(1)



#Keep checking the status of the classifier until the training is done
status = "Training"
s = requests.session()
while status == "Training":
	r = s.request(method='GET', url=bluemix.url + '/' + newClassifier, auth=(bluemix.user, bluemix.pwd))
    #If the serviice returns a 200 OK, let's process the json payload
	if r.status_code == 200:
		try:
			data = json.loads(r.text)
			status = data['status']
			print data['status_description']
		except Exception, e:
			print e
			status = "ERROR"
			sys.exit(1)

		#If we are still training, let's wait 60 seconds
        if status == "Training":
			time.sleep(60)
        else:
			print "Done training"

#We are done training, was the training successful?
if status == "Available":
	print "The classifier %s is now available and ready to accept Classify requests" % newClassifier
else:
	print "The classifier %s is NOT ready, please delete it, resolve the issue and re-submit a new classifier for training" % newClassifier



