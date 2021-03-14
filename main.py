from fbchat import log, Client
import fbchat
from fbchat.models import *
from models.service.IbotService import *


class CustomClient(Client):


    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):

        costs = IbotService.getPrice()
        frequentQuestions = IbotService.frequentQuestions()
        defaultMessage = IbotService.getDefaultMessage()
        
        if author_id != self.uid:
            if message_object.text in frequentQuestions :
             fbchat.Client.send(self, message=Message(text=costs), thread_id=thread_id, thread_type=thread_type)

            else :
                fbchat.Client.send(self, message=Message(text=defaultMessage), thread_id=thread_id, thread_type=thread_type)
                print('Se le ha enviado un mensaje a: '+ author_id +' y su ultimo mensaje fue: '+ message_object.text)
            
        else :
            #
            print('Envie: '+ message_object.text)


client = CustomClient(IbotService.getUserEmail(),IbotService.getUserPassword())
client.listen()