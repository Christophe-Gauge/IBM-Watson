#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Retrieves a list of the IBM Watson Natural Language Classifiers for a particular user
#and displays information about them. Requires valid credentials in the bluemix.py file.


import requests
import json
import bluemix


try:
	r = requests.get(bluemix.url, auth=(bluemix.user, bluemix.pwd))
	print r.status_code
	try:
		data = json.loads(r.text)
		for i in data['classifiers']:
		    print "\nclassifier_id: ", i['classifier_id']
		    print "name:          ", i['name']
		    print "language:      ", i['language']
 		    print "created:       ", i['created']
	except:
		print r.text
except Exception, e:
	print e


