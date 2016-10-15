import os
import json
import googleanalytics as ga

def credentialsX():
    if os.path.exists('credentials.json'):
        credentials = json.load(open('credentials.json'))
    else:
        credentials = ga.authorize()
        credentials = credentials.serialize()
        json.dump(credentials, open('credentials.json', 'w'))
    return credentials