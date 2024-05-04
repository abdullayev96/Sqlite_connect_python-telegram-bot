from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import  KeyboardButton, ReplyKeyboardMarkup

from translator  import  translate

TOKEN  = ''



def start_handler(update, context):

    update.message.reply_text(text="Hush kelibsz text kiriting !")
    # buttons  = [
    #     [KeyboardButton(text='Uzbek tili'), KeyboardButton(text="English")],
    #     [KeyboardButton(text='Arabic'), KeyboardButton(text="China")]
    # ]
    #
    # update.message.reply_text(
    #     text="Text yozing !",
    #     reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True, resize_keyboard=True)
    #
    #                           )
    # context.bot.send_message(update.message.chat_id, text='jimsz  nima qilyapsz qaramisz 😡😡😡😡👹👹👹👹🐣🐣🐣!!!')
    # context.bot.send_message(update.message.chat_id, text='yoq hech narsa')



def  message_handler(update, context):
    text = update.message.text
    translated =  translate(text)
    update.message.reply_text(translated)


updater = Updater(TOKEN)
dispatcher  =  updater.dispatcher


dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(MessageHandler(Filters.text,  message_handler))

updater.start_polling()





