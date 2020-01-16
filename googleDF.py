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



def getIntentsInBot():
	url = "https://console.dialogflow.com/api/intents"

	headers = {
    'authorization': "Bearer "+botIdDF,
    'cookie': "zUserAccessToken=55222461-14c3-4d71-ad86-39df2d2b6a81"
    }

	response = requests.get( url, headers=headers)
	print(response.text)
