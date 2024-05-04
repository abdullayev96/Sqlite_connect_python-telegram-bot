# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
# from telegram import InlineKeyboardMarkup, InlineKeyboardButton
#
#
# def start_command(update, context):
#     buttons=[
#         [InlineKeyboardButton(text="Compyuter mutaxassislari kanali ", callback_data="ib1")],
#         [InlineKeyboardButton(text="Compyuter dasturlari kanali", callback_data="ib2")],
#         [InlineKeyboardButton(text="Compyuter test kanali", callback_data="ib3")],
#         [InlineKeyboardButton(text="Foydali dasturlar ", callback_data="ib4")],
#     ]
#     user=update.message.from_user
#     update.message.reply_html('Botimizdan foydalanish uchun rasmiy kanalimizga \n  \n obuna boling <b> {} !!! </b>'
#                               .format(user.first_name),
#                                 reply_markup=InlineKeyboardMarkup(buttons)
#     )
#
# def inline_messages(update, context):
#     query=update.callback_query
#     print(query.message.text)
#     print(query.data)
#     if query.data == "ib1":
#         query.message.reply_photo(
#             photo=open("D:\\file\\image.jpg.jpg", "rb"),
#             caption="delx.uz, https://youtu.be/m9Wzkmj3oGw")
#
#         query.message.reply_photo(
#             photo=open("D:\\file\\super.jpg", "rb"),
#             caption="https://t.me/www_buymax")
#         # buttons = [
#         #     [InlineKeyboardButton(text="Inline Button 1.1", callback_data="ib1.1")],
#         #     [InlineKeyboardButton(text="Inline Button 1.2", callback_data="ib1.2")],
#         #     [InlineKeyboardButton(text="Inline Button 1.3", callback_data="ib1.3")],
#         #     [InlineKeyboardButton(text="Inline Button 1.4", callback_data="ib1.4")],
#         # ]
#         # query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
#     elif query.data == "ib2":
#         query.message.reply_document(document=open("D:\\file\\kitob.pdf", "rb"), caption="https://youtu.be/m9Wzkmj3oGw")
#         # buttons = [
#         #     [InlineKeyboardButton(text="Inline Button 2.1", callback_data="ib2.1")],
#         #     [InlineKeyboardButton(text="Inline Button 2.2", callback_data="ib2.2")],
#         #     [InlineKeyboardButton(text="Inline Button 2.3", callback_data="ib2.3")],
#         #     [InlineKeyboardButton(text="Inline Button 2.4", callback_data="ib2.4")],
#         # ]
#         # query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
#     elif query.data == "ib3":
#         # buttons = [
#         #     [InlineKeyboardButton(text="Inline Button 3.1", callback_data="ib3.1")],
#         #     [InlineKeyboardButton(text="Inline Button 3.2", callback_data="ib3.2")],
#         #     [InlineKeyboardButton(text="Inline Button 3.3", callback_data="ib3.3")],
#         #     [InlineKeyboardButton(text="Inline Button 3.4", callback_data="ib3.4")],
#         # ]
#         query.message.reply_video(video=open("D:\\file\\video.mp4", "rb"), caption="Bu zor video qalbiz rohatlanadi")
#
#     elif query.data == "ib4":
#         buttons = [
#             [InlineKeyboardButton(text="Inline Button 2.1", callback_data="ib2.1")],
#             [InlineKeyboardButton(text="Inline Button 2.2", callback_data="ib2.2")],
#             [InlineKeyboardButton(text="Inline Button 2.3", callback_data="ib2.3")],
#             [InlineKeyboardButton(text="Inline Button 2.4", callback_data="ib2.4")],
#
#         ]
#         query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
#
#
# def main():
#     updater = Updater("5168783191:AAG_9O8wpy-pE5h-4o2qGoTXKeJYXxE-B30")
#     dispatcher = updater.dispatcher
#
#     dispatcher.add_handler(CommandHandler("start", start_command))
#     dispatcher.add_handler(CallbackQueryHandler(inline_messages))
#
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__== '__main__':
#     main()

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


Token = "5168783191:AAG_9O8wpy-pE5h-4o2qGoTXKeJYXxE-B30"
updater = Updater(Token)
dispatcher = updater.dispatcher



# def start_command(update, context):
#     buttons=[
#         [InlineKeyboardButton(text="Compyuter mutaxassislari kanali ", callback_data="ib1")],
#         [InlineKeyboardButton(text="Compyuter dasturlari kanali", callback_data="ib2")],
#         [InlineKeyboardButton(text="Compyuter test kanali", callback_data="ib3")],
#         [InlineKeyboardButton(text="Foydali dasturlar ", callback_data="ib4")],
#     ]
#     user=update.message.from_user
#     update.message.reply_html('Botimizdan foydalanish uchun rasmiy kanalimizga \n  \n obuna boling <b> {} !!! </b>'
#                               .format(user.first_name),
#                                 reply_markup=InlineKeyboardMarkup(buttons)
#     )



def start_command(update, context):
    buttons=[
        [InlineKeyboardButton(text="Dasturlash", callback_data="ib1"), InlineKeyboardButton(text="Dastulash savodxonlik darslar", callback_data="ibn5")],
        [InlineKeyboardButton(text="3D max ", callback_data="ib2"), InlineKeyboardButton(text="Web Dizayn", callback_data="ibn6")],
        [InlineKeyboardButton(text="Chet ellar ", callback_data="ib3"), InlineKeyboardButton(text="Video mantaj", callback_data="ibn7")],
        [InlineKeyboardButton(text="Video mantaj ", callback_data="ib4"), InlineKeyboardButton(text="Biz bilan bog'lanish")],
    ]
    user=update.message.from_user
    update.message.reply_html('Botimizdan foydalanish uchun rasmiy kanalimizga \n  \n obuna boling <b> {} !!! </b>'
                              .format(user.first_name),
                                reply_markup=InlineKeyboardMarkup(buttons)
    )


def inline_messages(update, context):
    query=update.callback_query
    print(query.message.text)
    print(query.data)
    if query.data == "ib1":
        buttons = [
            [InlineKeyboardButton(text="Beckand/Fronted", callback_data="ib1.1")],
            [InlineKeyboardButton(text="Inline Button 1.2", callback_data="ib1.2")],
            [InlineKeyboardButton(text="Inline Button 1.3", callback_data="ib1.3")],
            [InlineKeyboardButton(text="Inline Button 1.4", callback_data="ib1.4")],
            [InlineKeyboardButton(text="Back", callback_data="back")],
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
        # query.message.reply_photo(
        #     photo=open("D:\\file\\image.jpg.jpg", "rb"),
        #     caption="delx.uz, https://youtu.be/m9Wzkmj3oGw")
        #
        # query.message.reply_photo(
        #     photo=open("D:\\file\\super.jpg", "rb"),
        #     caption="https://t.me/www_buymax")
        # buttons = [
        #     [InlineKeyboardButton(text="Inline Button 1.1", callback_data="ib1.1")],
        #     [InlineKeyboardButton(text="Inline Button 1.2", callback_data="ib1.2")],
        #     [InlineKeyboardButton(text="Inline Button 1.3", callback_data="ib1.3")],
        #     [InlineKeyboardButton(text="Inline Button 1.4", callback_data="ib1.4")],
        # ]
        # query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    elif query.data == 'back':
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup())
    elif query.data == "ib2":
        query.message.reply_document(document=open("D:\\file\\kitob.pdf", "rb"), caption="https://youtu.be/m9Wzkmj3oGw")
        # buttons = [
        #     [InlineKeyboardButton(text="Inline Button 2.1", callback_data="ib2.1")],
        #     [InlineKeyboardButton(text="Inline Button 2.2", callback_data="ib2.2")],
        #     [InlineKeyboardButton(text="Inline Button 2.3", callback_data="ib2.3")],
        #     [InlineKeyboardButton(text="Inline Button 2.4", callback_data="ib2.4")],
        # ]
        # query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    elif query.data == "ib3":
        buttons = [
            [InlineKeyboardButton(text="English tili", callback_data="ib1.1")],
            [InlineKeyboardButton(text="Rus tili", callback_data="ib1.2")],
            [InlineKeyboardButton(text="Arab tili", callback_data="ib1.3")],
            [InlineKeyboardButton(text="Fransuz tili", callback_data="ib1.4")],
            [InlineKeyboardButton(text=" 🔙 Orqaga", callback_data="ib1.5"), InlineKeyboardButton(text=" 🔝 Bosh Menu", callback_data="ib1.6")],

        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
        #query.message.reply_video(video=open("D:\\file\\video.mp4", "rb"), caption="📹 Windows 11 o'rnatish o'zbek tilida \n 👤 Muallif: Olim Abdanov \n Sayt: olimabdanov.uz \n Telbit.ly/3AE7cur \n YouTube: bit.ly/3CnI64e \n @BepulDarslarBot — IT darslar platformasi!")

    elif query.data == "ib4":
        buttons = [
            [InlineKeyboardButton(text="Inline Button 2.1", callback_data="ib2.1")],
            [InlineKeyboardButton(text="Inline Button 2.2", callback_data="ib2.2")],
            [InlineKeyboardButton(text="Inline Button 2.3", callback_data="ib2.3")],
            [InlineKeyboardButton(text="Inline Button 2.4", callback_data="ib2.4")],

        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))





dispatcher.add_handler(CommandHandler('start', start_command))
dispatcher.add_handler(CallbackQueryHandler(inline_messages))

updater.start_polling()



