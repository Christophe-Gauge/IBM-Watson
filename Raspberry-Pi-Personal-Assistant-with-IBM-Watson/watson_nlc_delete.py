#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Sends Classify requests to a trained and available IBM Watson Natural Language Classifier.
#Requires valid credentials in the bluemix.py file.
#
#Usage: watson_nlc_delete.py <Classifier_ID>
#   where <Classifier_ID> is a previously created Classifier (see watson_nlc_create.py and watson_nlc_list.py)

import requests
import json
import sys

import bluemix

if len(sys.argv) != 2:
	print 'watson_nlc_delete.py <Classifier_ID>'
	sys.exit(2)

#Construct the URL based on the argument provided
print sys.argv[1]
url = bluemix.url  + '/' + sys.argv[1]

#Send the DELETE request
try:
	r = requests.delete(url, auth=(bluemix.user, bluemix.pwd))
	print r.status_code
	if r.status_code == 200:
		print "Deleted"
	else:
		print "Delete failed"
		print r.text
except Exception, e:
	print e


