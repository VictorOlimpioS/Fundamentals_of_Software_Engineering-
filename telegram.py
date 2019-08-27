import telepot
from chatbot import Chatbot

telegram = telepot.Bot('YOUR TOKEN')
bot = Chatbot("BOT NAME")

def receivingMsg(msg):
    phrase = bot.listenTo(phrase=msg['text'])
    asw = bot.think(phrase)
    bot.speak(asw)
    typeMsg, typeChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID,asw)
    return asw

telegram.message_loop(receivingMsg)

while True:
	pass
    

