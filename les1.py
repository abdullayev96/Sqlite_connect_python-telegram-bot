from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup



TOKEN  = ""


def start_handler(update, context):
   update.message.reply_text(text="😊😊 Assalamu alaykum hush kelibsiz botga \n qanday xizmat kerak")

   chat=update.message.from_user.id
   print(chat)


   # username = update.message.from_user.username
   #
   # #context.bot.send_message(chat_id=f"6282585041", text=f"Botga yangi user qoshildi chat ID={chat}")
   # context.bot.send_message(chat_id=chat, text=f"Botga Hush kelibsiz\n {username}")



def message_handler(update, context):
    text = update.message.text.upper()
    update.message.reply_text(text=f"Sizning xabaringiz={text}")



def menu_show(update, context):
    buttons =[
        [KeyboardButton(text="🪪 First name"), KeyboardButton(text="⌛️ Yosh")],

        [KeyboardButton(text="📞 Contact", request_contact=True),


         KeyboardButton(text="📍 Location", request_location=True)]
    ]


    update.message.reply_text(
            text="Menu",
            reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True))




def settings_handler(update, context):
   update.message.reply_text(text="Texnik xizmat bolimi")
   #context.bot.send_message(text=)



def help(update, context):
    update.message.reply_text(text=" 🧗‍♀️ Sizga qanday yordam kerak ?")




def contact_handler(update, context):
    num=update.message.contact.phone_number
    update.message.reply_text(text=f"Siz raqamingiz={num}")
    print(update.message.contact.phone_number)



def location_handler(update, context):
    location = update.message.location

    lat = update.message.location.latitude
    long = update.message.location.longutide

    update.message.reply_location(latitude=location.latitude, longitude=location.longutide)
    print(lat, long)



updater = Updater(TOKEN)
dispatcher  =  updater.dispatcher


dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('setting', settings_handler))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('menu', menu_show))



#dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
dispatcher.add_handler(MessageHandler(Filters.location,  location_handler))

updater.start_polling()

