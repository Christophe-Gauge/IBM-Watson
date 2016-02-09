#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Enter the IBM Watson Bluemix credentials and the URL of the Natural Language Classifier service you abtained
#from https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/services-catalog.html

Bluemix_CRED = "username:password"
url = 'https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers'
    
user = Bluemix_CRED.split(':')[0]
pwd = Bluemix_CRED.split(':')[1]

