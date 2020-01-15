#!/bin/env python

from configBot import *

import time, json
import watson_developer_cloud

assistant = assistant = watson_developer_cloud.AssistantV1(username=watson_uid, password=watson_passwd, version="2018-02-16")


def WatsonCreateBot(botname):
	watsonBotId =  assistant.create_workspace(botname,description=botname, language=lang)["workspace_id"]
	print("WatsonBotId:",watsonBotId)
	return watsonBotId
	

def WatsonFindIntent(watsonBotId, utterance):
	response = assistant.message(workspace_id=watsonBotId,input={"text": utterance},alternate_intents=False)
	if len(response["intents"])>0:
		#return response["intents"][0]
		return response["intents"]
	else: return [{"intent":"None","confidence":-1}]

def WatsonCleanIntent(intent, score_str="1"):
	cleanIntent = intent.replace(" ","").replace("\t","")
	if cleanIntent.lower() == "defaultfallbackintent":cleanIntent="None"

	if (score_str == "Null"): score = 0
	else: score = float(score_str)    
    
	if score < threshold and score > 0: cleanIntent="None"    
	return cleanIntent

def WatsonAddIntentAndUtterance(watsonBotId, intent,utterances):
	validIntent = WatsonCleanIntent(intent)
	assistant.create_intent(watsonBotId, validIntent, description=validIntent, examples=[{"text":utterance} for utterance in utterances])

