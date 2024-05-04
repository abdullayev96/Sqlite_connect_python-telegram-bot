from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def start_command(update, context):
    buttons=[
        [InlineKeyboardButton(text="Inline Button 1", callback_data="ib1")],
        [InlineKeyboardButton(text="Inline Button 2", callback_data="ib2")],
        [InlineKeyboardButton(text="Inline Button 3", callback_data="ib3")],
        [InlineKeyboardButton(text="Inline Button 4", callback_data="ib4")],
    ]
    update.message.reply_text(
        text="Inline Button",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def inline_messages(update, context):
    query=update.callback_query
    print(query.message.text)
    print(query.data)
    if query.data == "ib1":
        buttons = [
            [InlineKeyboardButton(text="Inline Button 1.1", callback_data="ib1.1")],
            [InlineKeyboardButton(text="Inline Button 1.2", callback_data="ib1.2")],
            [InlineKeyboardButton(text="Inline Button 1.3", callback_data="ib1.3")],
            [InlineKeyboardButton(text="Inline Button 1.4", callback_data="ib1.4")],
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    elif query.data == "ib2":
        buttons = [
            [InlineKeyboardButton(text="Inline Button 2.1", callback_data="ib2.1")],
            [InlineKeyboardButton(text="Inline Button 2.2", callback_data="ib2.2")],
            [InlineKeyboardButton(text="Inline Button 2.3", callback_data="ib2.3")],
            [InlineKeyboardButton(text="Inline Button 2.4", callback_data="ib2.4")],
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    elif query.data == "ib3":
        buttons = [
            [InlineKeyboardButton(text="Inline Button 3.1", callback_data="ib3.1")],
            [InlineKeyboardButton(text="Inline Button 3.2", callback_data="ib3.2")],
            [InlineKeyboardButton(text="Inline Button 3.3", callback_data="ib3.3")],
            [InlineKeyboardButton(text="Inline Button 3.4", callback_data="ib3.4")],
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    elif query.data == "ib4":
        buttons = [
            [InlineKeyboardButton(text="Inline Button 2.1", callback_data="ib2.1")],
            [InlineKeyboardButton(text="Inline Button 2.2", callback_data="ib2.2")],
            [InlineKeyboardButton(text="Inline Button 2.3", callback_data="ib2.3")],
            [InlineKeyboardButton(text="Inline Button 2.4", callback_data="ib2.4")],
            [InlineKeyboardButton(text="Inline button 2.5", callback_data="ibn2.5")],
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


def main():
    updater = Updater("5168783191:AAG_9O8wpy-pE5h-4o2qGoTXKeJYXxE-B30")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CallbackQueryHandler(inline_messages))


    updater.start_polling()
    updater.idle()

if __name__== '__main__':
    main()