from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup



def start_command(update, context):
    buttons = [
        [KeyboardButton(text="Contact", request_contact=True), KeyboardButton(text="Name")],
        [KeyboardButton(text="Location", request_location=True), KeyboardButton(text="Address")]
    ]


    update.message.reply_text(
        text="Tanlang!!!",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
    )



def message_handler(update, context):
    message = update.message.text
    print(message)
    update.message.reply_text(text=f'Sizning xabaringz   {message}')


def contact_handler(update, context):
    contact = update.message.contact.phone_number
    print(contact)
    update.message.reply_text(f'Sizning raqamingz {contact}')
    context.bot.send_message(chat_id = update.message.chat_id, text= f'{contact}')


def location_handler(update, context):
    location = update.message.location
    print(location)
    update.message.reply_location(latitude=location.latitude, longitude=location.longitude)


def main():
    updater=Updater("") ##token beriladi
    dispatcher=updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))


    updater.start_polling()
    updater.idle()

if __name__== '__main__':
    main()
