import requests
from configBot import *

import dialogflow_v2 as dialogflow
intents_client = dialogflow.IntentsClient()


def addIntentAndUtteranceDF(DFIntent,DFUtterances):
    parent = intents_client.project_agent_path(botIdDF)
    training_phrases = []
    for utterance in DFUtterances:
        part = dialogflow.types.Intent.TrainingPhrase.Part(text=utterance)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.types.Intent.Message.Text(text="")
    message = dialogflow.types.Intent.Message(text=text)

    intent = dialogflow.types.Intent(
        display_name=DFIntent,
        training_phrases=training_phrases,
        messages=[message])

    response = intents_client.create_intent(parent, intent)    
    
    """
        url = "https://console.dialogflow.com/api/intents"
        string=[{"isTemplate":False,"data":[{"text":DFUtterances[i]}],"count":0,"id":None,"updated":None}
                                             for i in range(len(DFUtterances))]

        #Training utterances have to be sent in the above format. Hence saved for all trian utterances in a string and passed it on the payload.
        payload = {"name":DFIntent,"auto":True,"contexts":[],"templates":[],"responses":[{"parameters":[],"resetContexts":False,"affectedContexts":[],"messages":[],"speech":[],"defaultResponsePlatforms":{}}],"source":None,"priority":500000,"cortanaCommand":{"navigateOrService":"NAVIGATE","target":""},"events":[],"userSays":string}
        headers = {
    'authorization': "Bearer "+Token_DF,#Fetched from config file.
    'content-type': "application/json;charset=UTF-8",
            }
        try:    
                response = requests.post( url, json=payload, headers=headers,params= {"lang":lang.replace("_","-")})
                addFallbackIntent()
        except:
                raise Exception("Error while adding intent and utterances for google")
    """


def addFallbackIntent():
    parent = intents_client.project_agent_path(botIdDF)
    #training_phrases = []

    #text = dialogflow.types.Intent.Message.Text(text="")
    #message = dialogflow.types.Intent.Message(text=text)

    intent = dialogflow.types.Intent(
        display_name="Default Fallback Intent",
        training_phrases=[],
        messages=[],
        is_fallback=true)

    response = intents_client.create_intent(parent, intent)    


    """
        url = "https://console.dialogflow.com/api/intents"

        querystring ={"lang":lang.replace("_","-")}

        payload = "{\"name\":\"Default Fallback Intent\",\"auto\":true,\"contexts\":[],\"templates\":[],\"responses\":[{\"parameters\":[],\"resetContexts\":false,\"affectedContexts\":[],\"messages\":[{\"type\":0,\"speech\":[]}],\"speech\":[],\"defaultResponsePlatforms\":{}}],\"source\":null,\"priority\":500000,\"cortanaCommand\":{\"navigateOrService\":\"NAVIGATE\",\"target\":\"\"},\"fallbackIntent\":true,\"events\":[],\"followupEvent\":null,\"endInteraction\":false,\"userSays\":[]}"
        headers = {
                        'authorization': "Bearer "+Token_DF,#Fetched from config file.
                        'content-type': "application/json;charset=UTF-8",
            }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    """


def getIntentsInBot():
	url = "https://console.dialogflow.com/api/intents"

	headers = {
    'authorization': "Bearer "+botIdDF,
    'cookie': "zUserAccessToken=55222461-14c3-4d71-ad86-39df2d2b6a81"
    }

	response = requests.get( url, headers=headers)
	print(response.text)
