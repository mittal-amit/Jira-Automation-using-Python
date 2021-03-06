'''
Created on Jan. 21, 2022

@author: amitmittal
@description: Epic class creates epic in Jira using python
It accepts the variable from the test file
'''

import requests
from requests.auth import HTTPBasicAuth
from automation import key
import json


#1. Get the project key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys="Enter here"
#2. Get the issue id for the Epic
 
class Epic():
    
    url = "https://freetestingapi.atlassian.net/rest/api/2/issue"
    auth = HTTPBasicAuth("hi.amitmittal@gmail.com", key.Key().key)
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    def __init__(self, summary, desc, issueType, project_key, word):
        
        #self.name = name
        self.summary = summary
        self.desc = desc
        self.issueType = issueType
        self.project_key = project_key
        self.word = word
    
    def createEpic(self):
        payload = json.dumps( {
            
            "fields": {
                "summary": self.summary,
                "description": self.desc,
                "issuetype": {
                    "id": self.issueType,
                    },
                "project":{
                    "key": self.project_key
                    },
                "assignee": {
                    "id": key.Key().assign
                    },
                "labels":self.word 
                }
            }
        )
        
        response = requests.request(
           "POST",
           self.url,
           data=payload,
           headers=self.headers,
           auth=self.auth,
           )
        
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
            
