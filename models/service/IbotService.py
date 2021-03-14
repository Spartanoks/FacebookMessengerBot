from models.service.implements.BotServiceImpl import *

class IbotService :

    def getPrice():
        return BotServiceImpl.getPrice()

    def getDefaultMessage() :
        return BotServiceImpl.getDefaultMessage()
    
    def frequentQuestions() :
        return BotServiceImpl.frequentQuestions()
    
    def getUserEmail() :
        return BotServiceImpl.getUserEmail()

    def getUserPassword() :
        return BotServiceImpl.getUserPassword()