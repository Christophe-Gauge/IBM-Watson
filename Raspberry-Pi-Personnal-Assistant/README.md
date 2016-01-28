Raspberry Pi Personnal Assistant
========================================

Turn your Raspberry Pi into your own personnal assistant by leveraging the IBM Watson Natural Language Classifier API. 

The Classifier API enables you to use natural language to interract with your Pi.


## Requirements:

* **A Raspberry Pi** Actually this code should run fine on any Linux or OS-X system
* **Natural Language Classifier service credentials** - 
  Log into bluemix.net, create an NLC service instance, bind it to an app, click the "show credentials" link in the app's dashboard.
  Then put the username and password in the `bluemix.py` file. 
  

## Training the Natural Language Classifier model

Training a classifier requires you to provide some examples of how users would express a particular intent. For instance, if I want to ask about the events that are scheduled on my calendar today, I could use expressions such as "What's my schedule like today?" or "Today's calendar".

These sentences need to be organized in a Comma-separated value or CSV file. Each entry in this file will contain two parts, an example of how a user would ask that question, and the user's true intent, also known as the class.

Once you have gathered enough examples for each class, you will need to submit the CSV file to the Watson API for training. Watson will use your examples to train a model specifically tuned for your need.

In order to train a new classifier, edit the `training.csv` file and enter your own examples and classes. When you are ready, run the `watson_nlc_create.py` script. It will upload the CSV file, create a new classifier, and check the status until it is trained. Depending on the number of entries and classes in your file, this could take awhile.


If you don't want to wait, you can always use the 'watson_nlc_list.py' to get a list of your classifiers. A classifier will not be able to answer questions until it is fully trained.
    

## Using the trained Classifier

Once the model is trained, you are ready to send requests to it. When you send your model a question, it will return a list of the classes or intents that best match your question, along with a level of confidence for each class. 

Use the `watson_nlc_list.py` to get a list of your classifiers and their status. Copy the `classifier_id` from the classifier you intent to use, and then run `watson_nlc_classify.py classifier_id "Sample question"`

The classifier API will return the top matching class, as well as a list of the best matching classes and the model's confidence.


## Enhancements


Keep in mind that gathering the right data in the right amount to train a good classifier is more of an art than a science, it will take some time.

The class can be used to forward the request to the right service, but some additional processing of the user's request may be needed (do you need the weather forecast for today or tomorrow, and for which location?)

By combining the Speech to Text, Natural Language Classifier, and Text to Speech APIs, you can easily turn your Raspberry Pi into your own Siri, Cortana or Alex...the possibilities are endless!
