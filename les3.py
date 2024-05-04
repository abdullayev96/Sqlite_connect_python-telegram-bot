from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
from telegram import ReplyKeyboardMarkup,KeyboardButton

TOKEN = ""


def start_command(update, context):
    print(update.message)
    update.message.reply_text(text=" Siz/ start camandasini kiritdngz 😊🙃 !")




def show_menu(update, context):
    buttons=[
        [KeyboardButton(text="Menu 1"), KeyboardButton(text="Menu 2")],
        [KeyboardButton(text="Menu 3"),KeyboardButton(text="Menu 4")],

    ]
    update.message.reply_text(
        text="Menu",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True,
                                         one_time_keyboard=False)

    )

def message_handler(update, context):
    message=update.message.text
    update.message.reply_text(text=f"Sizning xabaringiz: '{message}'")



updater=Updater("")
dispatcher=updater.dispatcher


dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(CommandHandler("menu", show_menu))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

updater.start_polling()

