from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram import  InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto


TOKEN = "5803370010:AAF3wpOiJs8eBoa98hsGYhrgimyYUN2vO8E"

updater = Updater(TOKEN)
dispatcher = updater.dispatcher



def start(update, context):

    update.message.reply_text(text="Yozgan chatlar saqlanib olinadi")



def message_chat(update, context):
    #update.message.reply_text("Enter your text")

    # if context.user_data.get('text'):
    #      words = context.user_data.get('text')
    #
    # else:
    #     words = []
    # words.append(update.message.text)
    # context.user_data['text'] =  words
    # print(context.user_data.get('text'))



    words = []
    words.append(update.message.text)
    context.user_data['text']  = words
    if context.user_data.get('text'):
         words = context.user_data.get('text')

    else:
        words = []
    words.append(update.message.text)
    context.user_data['text'] =  words

    print(context.user_data.get('text'))



def inline_handler(update, context):
    query = update.callback_query
    print(query)



dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, message_chat))
dispatcher.add_handler(CallbackQueryHandler(inline_handler))

updater.start_polling()

