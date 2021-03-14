from models.dao.asks import *
from models.dao.auth import *

class BotServiceImpl :

    def getPrice() :
        return Quests.getPrice()

    def getDefaultMessage() :
        return Quests.getDefaultMessage()
    
    def frequentQuestions() :
        return Quests.costAsks()
    
    def getUserEmail() :
        return Auth.USER_EMAIL

    def getUserPassword() :
        return Auth.USER_PASSWORD