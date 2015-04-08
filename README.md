# A promotional email classifier

## Overview
It fetches email from gmail API, classify it according to training dataset of promotional and other emails, extract information based on user interest like coupons codes, or any other keywords and display these emails on a dashboard.
Further predefined rules can be added like download the attachment (if any ) whenever a specific sender sends an email and stores that to a user specified location.

## Framework and libraries used
* Django web framework
* scikit-learn
* NLTK
* flanker
* Beautiful Soup
* python-dateutil

## Working
Text is extracted from raw emails using flanker and Beautiful Soup, then after preprocessing ( stop word removal, stemming etc ) text data is stored in Postgresql database. This data is then used as training data to classify new emails. After classification email is searched for user defined keywords and accordingly information is extracted from them and displayed on a separate dashboard. 
