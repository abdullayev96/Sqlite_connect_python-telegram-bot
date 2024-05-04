#### 1-chi holat
# from telegram.ext import Updater, CommandHandler
#
#
# def start_command(update, context):
#     print(update.message)
#     print(update.message.from_user)
#     update.message.reply_text(text=" Siz/ start camandasini kiritdngz 😊🙃 !")
#     context.bot.send_message(chat_id="", text="Ikkinchi xabar")
#
#
# def main():
#     updater=Updater("1828443311:AAFC_9GaPz03an-SZrGpaBWsaONDmJt9xzM")
#     dispatcher=updater.dispatcher
#
#     dispatcher.add_handler(CommandHandler("start", start_command))
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == '__main__':
#     main()

#
#
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#
#
# TOKEN = '1828443311:AAFC_9GaPz03an-SZrGpaBWsaONDmJt9xzM'
#
#
#
# def start_handler(update, context):
#     update.message.reply_text("Sz  start camandasini kiritdngz 😊🙃 !")
#     #context.bot.send_message(chat_id='814131561', text="szga xabar")
#     print(update.message)
#


# # def message_handler(update, context):
# #     text= update.message.text
# #     update.message.reply_text(f" sizning xabaringz= {text}")
# #
#
#
# def main():
#     updater=Updater(TOKEN)
#     dispatcher  = updater.dispatcher
#
#     dispatcher.add_handler(CommandHandler('start', start_handler))
#     # dispatcher.add_handler(MessageHandler(Filters.command, start_handler))
#     # dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
#
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__== '__main__':
#     main()





# from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
# from telegram import  ReplyKeyboardMarkup, KeyboardButton
#
#
#
#
# updater = Updater(TOKEN)
# dispatcher = updater.dispatcher
#
#
# def start(update, context):
#     text = update.message.text
#
#     context.bot.send_message(chat_id=update.message.chat_id, text="Siz start comandasini bosdzgz !!!")
#
# # def message_handler(update, context):
# #     text = update.message.text
# #     update.message.reply_text(text=f'Sizning habaringz={text}')
#
#
# def show_menu(update, context):
#     buttons = [
#         [KeyboardButton(text="Siz kutgan onlar ", request_contact=True,), KeyboardButton(text="Send location", request_location=True)],
#         [KeyboardButton(text="Menu3"), KeyboardButton(text="Menu4 ")]
#     ]
#
#
#     update.message.reply_text(
#         text="Menu tanlang ",
#         reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True
#             # resize_keyboard=True
#         )
#
#     )
#     print(buttons)
#
# def contact_handler(update, context):
#     number = update.message.contact
#     update.message.reply_text(text=f'Sizning contagingz {number}')
#     print(number)
#
#
# #def location_handler(update, context):
#     # location = update.message.location
#     # update.message.reply_location(latitude=location.latitude, longitude=location.longitude)
#     # print(location)
#     #
# def location_handler(update, context):
#     location = update.message.location
#     update.message.reply_location(longitude=location.longitude, latitude=location.latitude)
#     print(location)
#
#
#
# dispatcher.add_handler(CommandHandler('start', start))
# dispatcher.add_handler(CommandHandler('show', show_menu))
# #dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
# dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
# dispatcher.add_handler(MessageHandler(Filters.location, location_handler))
#
# updater.start_polling()
#
#



# def  start_handler(update, context):
#     update.message.reply_text(text="Siz start commandasini bosdingz ")
#     context.bot.send_message(chat_id=update.message.chat_id,  text="Hello man " )
#     print(update)
#
#
# def message(update, context):
#     text = update.message.text
#     update.message.reply_text(text=f'Sizning  javobingz={text}')
#
#
# def main():
#     updater = Updater(TOKEN)
#     dispatcher = updater.dispatcher
#
#     dispatcher.add_handler(CommandHandler('start', start_handler))
#
#     dispatcher.add_handler(MessageHandler(Filters.text, message))
#     # dispatcher.add_handler(MessageHandler(Filters.command, message))
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__== '__main__':
#     main()
#


from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram import  InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto


TOKEN = "5586056890:AAH1aeyV46pz-d_J_E4c849y6G6mDSzac5w"

updater = Updater(TOKEN)
dispatcher = updater.dispatcher


def start(update, context):

    buttons = [
        [InlineKeyboardButton(text="🍫 Shokalad ", callback_data="ibn1")],
        [InlineKeyboardButton(text="🍿 KFC", callback_data="ibn2")],
        [InlineKeyboardButton(text="🍦 Marojni ", callback_data="ibn3")],
        [InlineKeyboardButton(text="🍰  shirinlik ", callback_data="ibn4")]
    ]

    update.message.reply_photo(photo=open("D:\\file\\1.jpg.jpg", "rb"),
        caption='yangi rasm  ',
        reply_markup=InlineKeyboardMarkup(buttons)
    )

    # buttons = [
    #     [InlineKeyboardButton(text="Buuton 👨🏻‍💻 ", callback_data='in1')],
    #     [InlineKeyboardButton(text="👨🏻‍💻 Buuton ", callback_data='in2')],
    #     [InlineKeyboardButton(text="👨🏻‍💻 Buuton ", callback_data='in3')],
    #     [InlineKeyboardButton(text="👨🏻‍💻  Buuton ", callback_data='in4')]
    #
    # ]
    # update.message.reply_text(
    #     text="Menu buttons",
    #     reply_markup=InlineKeyboardMarkup(buttons)
    #
    #
    #     )

def inline_handler(update, context):
    query = update.callback_query
    # print(query)

    if query.data == 'ibn1':
        print("Edit ", update)
        buttons = [
            [InlineKeyboardButton(text="🍫  Mevali Shokalad ", callback_data="ibn1.1")],
            [InlineKeyboardButton(text=" Olchali ", callback_data="ibn1.2")],
            [InlineKeyboardButton(text="🍦 Qaymoqli  ", callback_data="ibn1.3")],
            [InlineKeyboardButton(text="🍰 Kofe li  ", callback_data="ibn1.4")]
        ]
        query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons))

#     elif query.data == 'ibn1.1':
#         query.message.reply_photo(photo=open("D:\\file\\1.jpg.jpg", "rb"),
# #             caption="https://t.me/www_buymax")
#            )
#
#     elif query.data == 'ibn1.2':
#         query.message.reply_video(video=open("D:\\file\\video.mp4", "rb"),
#         caption="Bu zor video qalbiz rohatlanadi")
#
#     elif query.data == 'ibn1.3':
#         query.message.reply_document(document=open("D:\\file\\Burhon_cv.docx", "rb"),
#             caption="https://youtu.be/m9Wzkmj3oGw")
#
#
#     elif query.data == 'ibn1.4':
#         query.message.reply_audio(audio=open("D:\\file\\audio.mp3.mp3", "rb"),
#             caption="https://youtu.be/m9Wzkmj3oGw")

    elif query.data == 'ibn4':
        print("edit 2", update)
        buttons = [
            [InlineKeyboardButton(text="Shokalad ", callback_data="ibn1.1")],
            [InlineKeyboardButton(text="Acchiq shokalad", callback_data="ibn1.2")],
            [InlineKeyboardButton(text="Yumshoq shirinlik ", callback_data="ibn1.3")],
            [InlineKeyboardButton(text="Qattiq shirinlik", callback_data="ibn1.4")]
        ]

        query.message.edit_media(media=InputMediaPhoto(media=open("D:\\file\\2.jpg.jpg", "rb"),
                                  caption="Edit media"),
                                 reply_markup=InlineKeyboardMarkup(buttons))


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(inline_handler))
# dispatcher.add_handler(CommandHandler('show', show_menu))
#dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
# dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
# dispatcher.add_handler(MessageHandler(Filters.location, location_handler))

updater.start_polling()



