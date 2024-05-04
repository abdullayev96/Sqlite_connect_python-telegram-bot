from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton


def start_command(update, context):
    print(update.message)
    update.message.reply_text(text=f" Siz/ start commandasini kiritdz")
    # context.bot.send_message(chat_id="", text="bu szni xabaringz")
#


# def help_command(update, context):
#     update.message.reply_text(text=f"siz/ help commandasini bosdngz!!!!")
#


# def setting_command(update, context):
#     update.message.reply_text(text=f"Siz/setting ni bosdngz !!!")
#


# def show_menu(update, context):
#     buttons=[
#         [KeyboardButton(text="Send first_name"), KeyboardButton(text="Send last_name")],
#         [KeyboardButton(text=" send age"), KeyboardButton(text="Send Contact", request_contact=True)],
#     ]
#     update.message.reply_text(
#         text="Menu",
#         reply_markup=ReplyKeyboardMarkup(buttons)
#     )
#
# def contact_handler(update, context):
#     phone_number=update.message.contact
#     update.message.reply_contact(text=f"Bu sizni raqamingz '{phone_number}'")


# def main():
#     updater=Updater("1828443311:AAFC_9GaPz03an-SZrGpaBWsaONDmJt9xzM")
#     dispatcher=updater.dispatcher
#
#     dispatcher.add_handler(CommandHandler("start", start_command))
#     # dispatcher.add_handler(CommandHandler("help", help_command))
#     # dispatcher.add_handler(CommandHandler("setting", setting_command))
#     # dispatcher.add_handler(MessageHandler(Filters.text, show_menu))
#     # dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
#     #
#
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__==' __main__':
    #main()