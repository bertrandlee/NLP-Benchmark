import requests, time, json, os
from configBot import *
import logging

headersChatlayer = {
    "content-type": "application/json",
    "Authorization": ""
}

def trainChatlayer(session, intents, utterances, botName, authTokenChatlayer):
    print("Starting to train chatlayer")
    trainBody = {
        "culture": "en-us",
        "examples": []
    }
    for intent, utterance in zip(intents, utterances):
        trainBody["examples"].append({"text": utterance,
                         "label": intent,
                         "entities": []})

    headersChatlayer["Authorization"] = "Basic " + authTokenChatlayer
    r = requests.post(
        url="https://nlp.master.chatlayer.ai/train/govtech/{}".format(botName),
        headers=headersChatlayer,
        json=trainBody
    ).json()

    botId = r.get("model_name", None)
    if botId is None:
        print("Failed to train Chatlayer bot")

    print("Submitted training request for Chatlayer: {}".format(botName))
    poll = "Waiting"
    while poll == "Waiting" or poll == "In Progress": poll = pollTrainingStatusChatlayer(session, botName, botId, authTokenChatlayer)
    if poll == "Finished":
        print("Chatlayer training finished")
    else:
        print("Chatlayer training Failed:" + poll)


def pollTrainingStatusChatlayer(session, botName, botId, authTokenChatlayer):
    time.sleep(2)
    url = os.path.join("https://nlp.master.chatlayer.ai", "status", "govtech", botName, botId)
    headersChatlayer["Authorization"] = "Basic " + authTokenChatlayer
    response = requests.get(url, headers=headersChatlayer)
    print(response.text)
    response = response.json()
    status = response.get("status", None)
    print("Polling Chatlayer, status {}".format(status))
    if status == "ok":
        return "Finished"
    elif status in ["not trained", "training", "trained", "loading", "loaded"]:
        return "Waiting"
    else:
        return "Failed"


def ChatlayerFindIntent(botName, utterance, authTokenChatlayer):
    body = {"text": utterance}
    url = os.path.join("https://nlp.master.chatlayer.ai", "extract", "govtech", botName)
    headersChatlayer["Authorization"] = "Basic " + authTokenChatlayer
    try:
        response = requests.post(url=url, json=body, headers=headersChatlayer).json()
        topscoring = response.get("topScoringIntent", None)
        intent =  topscoring.get("intent", "None")
        score = topscoring.get("score", -1)
        return intent, score
    except Exception:
        return "None", -1

