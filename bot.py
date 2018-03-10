from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
	text = "вызван /start"
	print("Привет !")
	update.message.reply_text("Привет! Я бот повторюшка - Карюшка Амбарцумюшка, напиши мне, что-нибудь, для начала конструктивного диалога)")

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text + ' ,а во всем виноват @karen_learn_bot')

# def solar_sys(bot, update):
# 	text = "/planet"
# 	print("Привет !")
# 	update.message.reply_text()

# 	if user_message[1] == 'neptune':
# 		user_text = ephem.Neptune(date)
# 		user_text = str(user_text)
# 		print(user_text)
# 		update.message.reply_text(user_text)

# 	if user_message[1] == 'uranus':
# 		user_text = ephem.Uranus(date)
# 		user_text = str(user_text)
# 		print(user_text)
# 		update.message.reply_text(user_text)

# 	if user_message[1] == 'saturn':
# 		user_text = ephem.Saturn(date)
# 		user_text = str(user_text)
# 		print(user_text)
# 		update.message.reply_text(user_text)

# 	if user_message[1] == 'jupiter':
# 		user_text = ephem.Jupiter(date)
# 		user_text = str(user_text)
# 		print(user_text)
# 		update.message.reply_text(user_text)

# 	if user_message[1] == 'mars':
# 		user_text = ephem.Mars(date)
# 		user_text = str(user_text)
# 		print(user_text)
# 		update.message.reply_text(user_text)

# 	if user_message[1] == 'earth':
# 		user_text = ephem.Earth(date)
# 		user_text = str(user_text)
# 		print(user_text)
# 		update.message.reply_text(user_text)

# 	if user_message[1] == 'venus':
# 		user_text = ephem.Venus(date)
# 		user_text = str(user_text)
# 		print(user_text)
# 		update.message.reply_text(user_text)

# 	if user_message[1] == 'merkury':
# 		user_text = ephem.Merkury(date)
# 		user_text = str(user_text)
# 		print(user_text)
# 		update.message.reply_text(user_text)

# 	if user_message[1] == 'sun':
# 		user_text = ephem.Sun(date)
# 		user_text = str(user_text)
# 		print(user_text)
# 		update.message.reply_text(user_text)



def main():
    updater = Updater("515349976:AAHLqcGXi0w6tvkos1oTTbJM8M-PcZbyp8s")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user)) 
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) 
    updater.start_polling()
    updater.idle()

main()