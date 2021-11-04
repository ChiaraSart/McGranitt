#!/usr/bin/python

import telepot

TOKEN = '*** 2017310938:AAFMJetMxqgyT11Ra6ikPR3s3q3fStSuyjs  ***'

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
       name = msg["from"]["first_name"]
        if '/hogwarts' in txt:
         bot.sendMessage(chat_id, '%s finalmente hai ricevuto la tua lettera per Hogwarts! Qua potrai imparare a sfruttare le tue abilità magiche al massimo e, alla fine della settimana, potrai metterti alla prova con dei test! Attraverso i risultati che otterrai, potrai far guadagnare punti alla tua casata: grifondoro, corvonero, tassorosso o serpeverde. Alla fine di ogni mese, la casata che avrà guadagnato più punti delle altre otterrà la coppa delle case!'%name)
        elif '/houses' in txt:
         import webbrowser

         url="https://docs.google.com/document/d/1b26R8ETF-7SBYhaunE1vS-Rs8RTUyhH-hQgc2lWdgZE/edit?usp=sharing";

         webbrowser.open (url)
        elif '/help' in txt:
         bot.sendMessage(chat_id, 'Se hai bisogno di informazioni sulla tua permanenza ad Hogwarts, digita /hogwarts; se, invece, vuoi entrare nella tua sala comune ma la scala dove stavi camminando ha deciso di spostarsi e hai perso la strada che porta alla tua torre, digita /houses e tornerai sulla giusta direzione')
        else:
         bot.sendMessage(chat_id, 'Non capisco cosa intendi dire, prova a digitare /help...')



if __name__ == '__main__'
 bot = telepot.Bot(TOKEN)
 bot.message_loop(on_chat_message)

print 'Listening ...'

import time
while 1:
    time.sleep(10)    

