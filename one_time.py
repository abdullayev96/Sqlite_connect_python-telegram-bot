from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


Token  =  "1828443311:AAFC_9GaPz03an-SZrGpaBWsaONDmJt9xzM"
updater = Updater(Token)
dispatcher = updater.dispatcher

main_buttons = [
    [KeyboardButton(text="Kitoblar", ), KeyboardButton(text="Telefonlar")],
    [KeyboardButton(text="Kiyimlar"), KeyboardButton(text="Mashinalar")],
]


def start_command(update, context):

    update.message.reply_text(
        text="Menu",  #### resize_keyboard razmirini togrilagani
        reply_markup=ReplyKeyboardMarkup(main_buttons, resize_keyboard=True)
    )
    #update.message.reply_text(text="Siz/ start commandasini kiritdz!!!")


# def help_command(update, context):
#     print(update)
#     update.message.reply_text(text="Siz/ help commandasini kiritdz qanday yoram kerak szga InshaaAlloh bartaraf etamz!!!")
#
# def setting_command(update, context):
#     print(update.message.text)
#     update.message.reply_text(text="Siz/ Setting commandasini kiritdz nosozlik chiqdimi 😎😎😎🙄🙄🙄😄😄😄")
#
# def show_menu(update, context):
#     buttons=[
#         [KeyboardButton(text="send contank", request_contact=True), KeyboardButton(text="Send location", request_location=True)],
#         [KeyboardButton(text="Menu 3"), KeyboardButton(text="Menu 4")],
#     ]
#     update.message.reply_text(
#         text="Menu",                   #### resize_keyboard razmirini togrilagani
#         reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
#     )

def message_handler(update, context):
    print(update.message.text)
    message=update.message.text
    buttons1 = [
        [
            InlineKeyboardButton(text="Apple", callback_data="ap1"),
            InlineKeyboardButton(text="Sumsung", callback_data="ap2"),
            InlineKeyboardButton(text="Nokia", callback_data="ap3"),
            InlineKeyboardButton(text="Xiomi", callback_data="ap4"),
        ],
        [
            InlineKeyboardButton(text="⬅️back", callback_data="end1")
        ]
    ]

    buttons2  = [
        [
            InlineKeyboardButton(text="Diniy kitoblar", callback_data="ap1")
        ],
        [
                InlineKeyboardButton(text="Ertak kitoblar", callback_data="ap2")
        ],
        [
            InlineKeyboardButton(text="G'azal kitoblar", callback_data="ap3")
        ],
        [
            InlineKeyboardButton(text="Matem kitoblar", callback_data="ap4")
        ],

        [
            InlineKeyboardButton(text="⬅️back", callback_data="end1")
        ]
    ]
    if message == "Telefonlar":
        update.message.reply_text(
            text="Tanlang:",
            reply_markup=InlineKeyboardMarkup(buttons1)
                                  )

    elif message == "Kitoblar":
        update.message.reply_text(
            text="Tanlang:",
            reply_markup=InlineKeyboardMarkup(buttons2)
        )

# def contact_handler(update, context):
#     print(update.message.contact)
#     phone_number=update.message.contact.phone_number
#     update.message.reply_text(text=f"sizni raqamingz '{phone_number}'")
#
# def location_handler(update, context):
#     print(update.message.location)
#     location=update.message.location
#     update.message.reply_location(latitude=location.latitude, longitude=location.longitude)
def inline_buttons(update, context):
    query  = update.callback_query


    if query.data == 'end1':
        query.message.reply_text(reply_markup=ReplyKeyboardMarkup(main_buttons))




dispatcher.add_handler(CommandHandler("start", start_command)) ### shu yerga start deb yozsak camandamz start boladi
# dispatcher.add_handler(CommandHandler("help", help_command))
# dispatcher.add_handler(CommandHandler("setting", setting_command))
# dispatcher.add_handler(CommandHandler("menu", show_menu))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler)) ### command  bolsa userga yozgani qaytarmidi
dispatcher.add_handler(CallbackQueryHandler(inline_buttons))
#dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler)) ###
#dispatcher.add_handler(MessageHandler(Filters.location, location_handler))

updater.start_polling()

