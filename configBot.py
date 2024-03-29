import json


with open("configBot.json", "r") as fp:
	conf = json.load(fp)

fileName =  conf["fileName"]  #conf["ML_Train.csv"]
TestFileName =  conf["TestFileName"]  #"ML_TestData.csv"
RESULTSFILE =  conf["RESULTSFILE"]  #""
debug =  conf.get("debug")  #True
botName =  conf["botName"]  #"BankBot"
lang =  conf["lang"]  #"en"
threshold =  conf["threshold"]  #"en"

# Platforms to enable
USEKORE =  conf["USEKORE"]  #True
USEGOOGLE =  conf["USEGOOGLE"]  #False
USELUIS =  conf["USELUIS"]  #False
USEWATSON =  conf["USEWATSON"]  #False
USEWIT =  conf["USEWIT"]  #False
USETAIGER = conf["USETAIGER"]
USECHATLAYER = conf["USECHATLAYER"]

# Kore.ai
KorePlatform =  conf["KorePlatform"]  #"https://bots.kore.ai"
ssoKore = conf["ssoKore"]
userIdKore = conf["userIdKore"] 
authTokenKore = conf["authTokenKore"] 
KoreEmailId = conf["KoreEmailId"]  #
KorePassword = conf["KorePassword"]  #
# optional platforms to enable to compare with kore
# Luis.ai
subscriptionToken= conf["subscriptionToken"]  #

# DialogFlow.ai
Token_DF =  conf["Token_DF"]  
Client_DF = conf["DF_CLIENT_ACCESS_TOKEN"]
botIdDF =  conf["botIdDF"]  

# Watson.ai
watson_uid =  conf["watson_uid"]  
watson_passwd =  conf["watson_passwd"]  

# Wit.ai
witUserToken =  conf["witUserToken"]  

#Taiger
taiger_uid = conf["taiger_uid"]
taiger_passwd = conf["taiger_passwd"]

# Chatlayer.ai
chatlayerToken = conf["chatlayerToken"]

