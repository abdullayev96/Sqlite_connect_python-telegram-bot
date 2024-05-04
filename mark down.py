from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import BotCommand
from deep_translator import GoogleTranslator
from telegram import KeyboardButton, ReplyKeyboardMarkup


TOKEN  = '6895917982:AAFGyKenodHjDuDHMbx-GI_Y-L7tH1ZfkE0'


# def show_menu(update, context):
#     buttons = [
#         [KeyboardButton(text="En"), KeyboardButton(text="Uz")],
#
#
#     ]
#
#     update.message.reply_text("Menu",
#         reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True))
#


def translate(text):
    tr = GoogleTranslator(source='uz', target='en').translate(text)
    return tr


def start_handler(update, context):

    update.message.reply_text(
        text="""<a href="http://www.delx.uz/">inline URL</a>""",
        parse_mode="HTML")


def super(update, context):
    text = update.message.text
    update.message.reply_text(translate(text=text))



# def message_handler(update, context):
#     text = update.message.text
#     print(text)
#
#     if text =='Uz':
#         update.message.reply_text(translate(text=text))

    #
    # elif text =="En":
    #     update.message.reply_text(translate(text=text))



updater = Updater(TOKEN)
dispatcher  =  updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(MessageHandler(Filters.text, super))


updater.start_polling()


## <i>Good job</i>, <code>None</code>, <s>100$</s> 90 $, <u>Ostiga tiziq</u>!