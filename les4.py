from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, KeyboardButton, ReplyKeyboardMarkup


TOKEN  = '5586056890:AAFsximPWCftQ3r5WbV3CKqlMw_msKGN9-4'


states = {
    "comment_text":1,
    "bxm_text":2,
    "employee_text":3,
    "customers_text":4,
    "service_text":5,
    "quality_service":6,

}

def start_handler(update, context):

    buttons = [
        [KeyboardButton(text="Tashkent"),KeyboardButton(text="Samarqand")],
        [KeyboardButton(text="Andijon"),
         KeyboardButton(text="Fargona")],
        [KeyboardButton(text="Namangan"),
         KeyboardButton(text="Jizzax")],
        [KeyboardButton(text="Sirdaryo"),
         KeyboardButton(text="Navoiy")],
        [KeyboardButton(text="Surxondaryo"),
         KeyboardButton(text="Qashqadaryo",)],
        [KeyboardButton(text="Xorazm",),
         KeyboardButton(text="Qoraqolpoq",)],
        [KeyboardButton(text="Buxoro")],
    ]


    update.message.reply_text(
        text="Viloyatlardan birini tanlang",
        reply_markup=ReplyKeyboardMarkup(buttons))


    if context.user_data.get('text'):
        words = context.user_data.get('text')

    else:
        words = []
    words.append(update.message.text)
    context.user_data['text'] = words
    print(context.user_data.get("text"))

    return states['comment_text']


def get_comment_text(update, context):
    message = update.message.text
    if message == "Tashkent":
        buttons = [
            [KeyboardButton(text="Tashkent"), KeyboardButton(text="Samarqand")],
            [KeyboardButton(text="Andijon"),
             KeyboardButton(text="Fargona")],
            [KeyboardButton(text="Namangan"),
             KeyboardButton(text="Jizzax")],

        ]
        update.message.reply_text(
        text="Bxm ni tanlang",
        reply_markup=ReplyKeyboardMarkup(buttons))


    elif message == "Samarqand":
        buttons = [
            [KeyboardButton(text="Bxm Termiz"), KeyboardButton(text="Bxm Samarqand")],
            [KeyboardButton(text="Bxm Andijon"),
             KeyboardButton(text="Bxm Fargona")],
            [KeyboardButton(text="Bmax Namangan"),
             KeyboardButton(text="Bxm Jizzax")],

        ]
        update.message.reply_text(
            text="Bxm ni tanlang",
            reply_markup=ReplyKeyboardMarkup(buttons))




    if context.user_data.get('text'):
        words = context.user_data.get('text')

    else:
        words = []
    words.append(update.message.text)
    context.user_data['text'] = words
    print(context.user_data.get("text"))

    return states['bxm_text']


def get_bxm_text(update, context):
    buttons = [
        [KeyboardButton(text="1 😣"), KeyboardButton(text="2☹️"), KeyboardButton(text="3 🙁")],
        [KeyboardButton(text="4 😑"), KeyboardButton(text="5 🤗", )]
    ]

    update.message.reply_text(text="Xodim muomilasi:",
                              reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))

    if context.user_data.get('text'):
        words = context.user_data.get('text')

    else:
        words = []
    words.append(update.message.text)
    context.user_data['text'] = words
    print(context.user_data.get("text"))

    return states['employee_text']



def get_employee_text(update, context):
    buttons = [
        [KeyboardButton(text="1 👊 "),
         KeyboardButton(text="2 👎"), KeyboardButton(text="3 👌🏻")],
        [KeyboardButton(text="4 🤙 "), KeyboardButton(text="5 👍 ")]

    ]

    update.message.reply_text(text="Mijozlar uchun sharoitlar:",
                              reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))


    if context.user_data.get('text'):
        words = context.user_data.get('text')

    else:
        words = []
    words.append(update.message.text)
    context.user_data['text'] = words
    print(context.user_data.get("text"))

    return states['customers_text']


def get_customer_text(update, context):
    buttons = [
        [KeyboardButton(text="1 🐌"),
         KeyboardButton(text="2 🐢"), KeyboardButton(text="3 🛺 ")],
        [KeyboardButton(text="4 🏎"), KeyboardButton(text="5 🚀")]]

    update.message.reply_text(text="Xizmat tezligi",
                              reply_markup=ReplyKeyboardMarkup(buttons,
                                                               one_time_keyboard=True, resize_keyboard=True))


    if context.user_data.get('text'):
        words = context.user_data.get('text')

    else:
        words = []
    words.append(update.message.text)
    context.user_data['text'] = words
    print(context.user_data.get("text"))


    return states['service_text']


def get_service_text(update, context):
    buttons = [
        [KeyboardButton(text="1 🐌"),
         KeyboardButton(text="2 🐢"), KeyboardButton(text="3 🛺 ")],
        [KeyboardButton(text="4 🏎"), KeyboardButton(text="5 🚀")]]

    update.message.reply_text(text="Xizmat sifati",
                              reply_markup=ReplyKeyboardMarkup(buttons,
                                                               one_time_keyboard=True, resize_keyboard=True))


    if context.user_data.get('text'):
        words = context.user_data.get('text')

    else:
        words = []
    words.append(update.message.text)
    context.user_data['text'] = words
    print(context.user_data.get("text"))


    return states['quality_service']



def get_quality_service(update, context):


    update.message.reply_text(text="Tashrifingiz  uchun raxmat")

    if context.user_data.get('text'):
        words = context.user_data.get('text')

    else:
        words = []
    words.append(update.message.text)
    context.user_data['text'] = words
    print(context.user_data.get("text"))


    return ConversationHandler.END



def stop_conversation(update, context):
    return ConversationHandler.END



def inline_handler(update, context):
    query = update.callback_query
    print(query)


    if query.data =="ibn1":
        buttons = [
            [InlineKeyboardButton(text="Qarshi Bxm", callback_data="ibn1"),
             InlineKeyboardButton(text="Koson Bxm", callback_data="ibn2")],
            [InlineKeyboardButton(text="Farhod Bxm", callback_data="ibn3"),
             InlineKeyboardButton(text="Nasaf Bxo", callback_data="ibn4")],

        ]
        query.message.reply_text(text="Bxm joyini kiriting:", reply_markup=InlineKeyboardMarkup(buttons), one_time_keyboard=True, resize_keyboard=True)

#
# updater = Updater(TOKEN)
# dispatcher  =  updater.dispatcher
#
# dispatcher.add_handler(CommandHandler('start', start_handler))
#
# dispatcher.add_handler(MessageHandler(Filters.text,  get_comment_text))
# dispatcher.add_handler(MessageHandler(Filters.text,  get_bxm_text))
# dispatcher.add_handler(MessageHandler(Filters.text,  get_employee_text))
# dispatcher.add_handler(MessageHandler(Filters.text,  get_customer_text))
# dispatcher.add_handler(MessageHandler(Filters.text,  get_service_text))
# dispatcher.add_handler(MessageHandler(Filters.text,  get_quality_service))
# dispatcher.add_handler(CallbackQueryHandler(inline_handler))
#
# updater.start_polling()



updater = Updater(TOKEN)
dispatcher = updater.dispatcher



dispatcher.add_handler(
    ConversationHandler(
        entry_points=[CommandHandler('start', start_handler)],
                states={
                    1: [MessageHandler(Filters.text, get_comment_text)],
                    2: [MessageHandler(Filters.text, get_bxm_text)],
                    3: [MessageHandler(Filters.text, get_employee_text)],
                    4: [MessageHandler(Filters.text, get_customer_text)],
                    5: [MessageHandler(Filters.text, get_service_text)],
                    6: [MessageHandler(Filters.text, get_quality_service)],


                },
        fallbacks=[CommandHandler('stop', stop_conversation)]
            )

    )

updater.start_polling()
updater.idle()

