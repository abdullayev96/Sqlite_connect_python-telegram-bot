from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler
from telegram import (
    InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
)
import re

states = {
    "first_name": 1,
    "last_name": 2,
    "age": 3,
    "gender": 4,
    "contact": 5,
    "inline": 6
}


def start_command(update, context):
    update.message.reply_text(
        text=f"Enter First Name",
        reply_markup=ReplyKeyboardRemove()

    )
    return states['first_name']


def get_first_name(update, context):
    context.user_data["first_name"] = update.message.text

    if context.user_data.get('edit_state'):
        send_edit_data(update, context)
        context.user_data['edit_state'] = False
        return states['inline']

    update.message.reply_text(
        text=f"Enter Last Name!",
        reply_markup=ReplyKeyboardRemove()

    )
    return states['last_name']


def get_last_name(update, context):
    context.user_data["last_name"] = update.message.text

    if context.user_data.get('edit_state'):
        send_edit_data(update, context)
        context.user_data['edit_state'] = False
        return states['inline']

    update.message.reply_text(
        text=f"Enter Your Age!",
        reply_markup=ReplyKeyboardRemove()
    )
    return states['age']


def get_age(update, context):
    context.user_data["age"] = update.message.text

    if context.user_data.get('edit_state'):
        send_edit_data(update, context)
        context.user_data['edit_state'] = False
        return states['inline']

    buttons = [
        [KeyboardButton(text="Male"), KeyboardButton(text="Female")]
    ]
    update.message.reply_text(
        text=f"Choose Your Gender!",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
    )
    return states['gender']


def get_error_age(update, context):
    update.message.reply_text(
        text=f"Please enter true value!!!",
    )
    return states['age']


def get_gender(update, context):
    context.user_data["gender"] = update.message.text

    if context.user_data.get('edit_state'):
        send_edit_data(update, context)
        context.user_data['edit_state'] = False
        return states['inline']

    buttons = [
        [KeyboardButton(text="Share", request_contact=True)]
    ]
    update.message.reply_text(
        text=f"Share Your Contact Or Send It",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
    )
    return states['contact']


def get_error_gender(update, context):
    update.message.reply_text(
        text=f"Please enter true value!!!",
    )
    return states['gender']


def get_contact(update, context):
    context.user_data["contact"] = update.message.contact.phone_number


    send_edit_data(update, context)
    context.user_data['edit_state'] = False
    return states['inline']


def get_text_contact(update, context):
    context.user_data["contact"] = update.message.text
    send_edit_data(update, context)
    context.user_data['edit_state'] = False
    return states['inline']


def send_edit_data(update, context):
    data = context.user_data
    buttons = [
        [
            InlineKeyboardButton(text="Edit Data", callback_data="edit_data"),
        ]
    ]

    msg = update.message.reply_text(
        text=f"<b>First Name</b>: {data['first_name']}\n"
             f"<b>Last Name</b>:{data['last_name']}\n"
             f"<b>Age</b>: {data['age']}\n"
             f"<b>Gender</b>: {data['gender']}\n"
             f"<b>Phone Number</b>: {data['contact']}",
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="HTML"
    )
    # update.message.reply_text(msg)
    context.bot.edit_message_reply_markup(
            chat_id=update.message.chat_id,
            message_id=msg.message_id,
            reply_markup=InlineKeyboardMarkup(buttons)
    )


def stop_conversation(update, context):
    return ConversationHandler.END


def inline_handler(update, context):

    query = update.callback_query

    if query.data == "edit_data":
        buttons = [
            [
                InlineKeyboardButton(text="First Name", callback_data="edit_first_name"),
                InlineKeyboardButton(text="Last Name", callback_data="edit_last_name"),
            ],
            [
                InlineKeyboardButton(text="Age", callback_data="edit_age"),
                InlineKeyboardButton(text="Gender", callback_data="edit_gender"),
            ],
            [
                InlineKeyboardButton(text="Contact", callback_data="edit_contact")
            ]
        ]
        query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif query.data == "edit_first_name":
        query.message.edit_text("Enter First Name!")
        context.user_data['edit_state'] = True
        return states['first_name']

    elif query.data == "edit_last_name":
        query.message.edit_text("Enter Last Name!")
        context.user_data['edit_state'] = True
        return states['last_name']

    elif query.data == "edit_age":
        query.message.edit_text("Enter Age!")
        context.user_data['edit_state'] = True
        return states['age']

    elif query.data == "edit_gender":
        buttons = [
            [KeyboardButton(text="Male"), KeyboardButton(text="Female")]
        ]
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text(text="Choose Your Gender!", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True))
        context.user_data['edit_state'] = True
        return states['gender']

    elif query.data == "edit_contact":
        buttons = [
            [KeyboardButton(text="Share", request_contact=True)]
        ]
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text("Share Your Contact Or Send It!", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True))
        context.user_data['edit_state'] = True
        return states['contact']


def main():
    updater = Updater("5914648388:AAE-kvvBEdZBlQwFx6ak4aIrG1FzhvXH8wk")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('start', start_command)],
            states={
                1: [MessageHandler(Filters.text, get_first_name)],
                2: [MessageHandler(Filters.text, get_last_name)],
                3: [MessageHandler(Filters.regex('^[0-9]+$'), get_age), MessageHandler(Filters.text, get_error_age)],
                4: [
                    MessageHandler(Filters.regex('^(Male|Female)$'), get_gender),
                    MessageHandler(Filters.text, get_error_gender)
                ],
                5: [MessageHandler(Filters.text, get_text_contact), MessageHandler(Filters.contact, get_contact)],
                6: [CallbackQueryHandler(inline_handler)]
            },
            fallbacks=[CommandHandler('stop', stop_conversation)],
        )
    )

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
