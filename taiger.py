import requests
from configBot import *


def TaigerCreateBot(botName):
    url = "https://iconverse-govtech.taiger.io/iconverse-admin/api/external/" 
    headers = {'content-type': "application/json"}    
    payload = {"clientId":taiger_uid, "clientSecret":taiger_passwd}
    
    try:    
            response = requests.post( url+"authenticate", json=payload, headers=headers)
            #print(response.text)
    except:
            raise Exception("Error while authenticating with Taiger")

    accessToken = response.json()['accessToken']
    print("accessToken= ", accessToken)
    
    headers["Authorization"] = "Bearer " + accessToken
    #print(headers)
    
    payload = {"botName":botName}
    
    try:    
            response = requests.post( url+"bots", json=payload, headers=headers)
            print(response.text)
    except:
            raise Exception("Error while creating bot for Taiger")
            
    botId = response.json()["id"]
    
    payload = {"botId":botId, "name":botName}

    try:    
            response = requests.post( url+"libraries", json=payload, headers=headers)
            #print(response.text)
    except:
            raise Exception("Error while creating library for Taiger")
            
    libraryId = response.json()["id"]
    
    return accessToken, botId, libraryId


def TaigerAddIntentAndUtterance(accessToken, libraryId, Intent, Utterances):
    url = "https://iconverse-govtech.taiger.io/iconverse-admin/api/external/" 
    headers = {'content-type': "application/json", "Authorization":"Bearer "+accessToken}    
 
    payload = {"libraryId": libraryId,"phrases": [],"question": Intent,
               "state": {"name": "string","text": "string"},"status": "published"}

    for u in Utterances:
        payload["phrases"].append({"text":u})
        
    try:    
            response = requests.post( url+"intents/setup", json=payload, headers=headers)
            #print(response.text)
    except:
            raise Exception("Error while setting up intents with Taiger")


def TaigerTrainBot(accessToken, botId):
    url = "https://iconverse-govtech.taiger.io/iconverse-admin/api/external/bots/"+botId+"/train" 
    headers = {'content-type': "application/json", "Authorization":"Bearer "+accessToken}    
     
    try:    
            response = requests.post( url, headers=headers)
            #print(response.text)
    except:
            raise Exception("Error while setting up intents with Taiger")


def TaigerFindIntent(accessToken, botId, utterance):
    url = "https://iconverse-govtech.taiger.io/iconverse-admin/api/external/bots/"+botId+"/message" 
    headers = {'content-type': "application/json", "Authorization":"Bearer "+accessToken}    

    try:    
            response = requests.post( url, json=utterance, headers=headers)
            #print(response.text)
    except:
            raise Exception("Error while finding intent with Taiger")
            
    if response.status_code != 200:
        raise Exception("Status code " + str(response.status_code) + " while finding Taiger intent")

    intent = response.json()["intentName"]
    
    if intent == "NoInfo" or intent == "Intent Search Fallback Template":
        intent = "None"
        
    return intent


