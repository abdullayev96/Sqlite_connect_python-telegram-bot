# from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
# from telegram import ReplyKeyboardMarkup,KeyboardButton
#
#
# def start_command(update, context):
#     print(update.message)             ##### bu qator esa text yuboradi
#     update.message.reply_text(text=" Siz/ start camandasini kiritdngz 😊🙃 !")
#     context.bot.send_message(chat_id="814131561", text="yaxshimisz salomATMISZ ")
#
#
# def show_menu(update, context):
#     buttons=[
#         [KeyboardButton(text="first name", request_contact=True), KeyboardButton(text="last name", request_location=True)], #### bu qator knupka vazifasini beradi
#         [KeyboardButton(text="Menu 3"),KeyboardButton(text="Menu 4")],
#
#     ]
#     update.message.reply_text(
#         text="Menu",
#         reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)   ### bu joyi razmer beriladi agar True bolsa
#                                                                       #### one_time_keyboard= true bir marta ochilib yopilish imkonini beradi
#     )
#
#
# def message_handler(update, context):
#     print(update.message)
#     print(update.message.from_user.id)
#     message=update.message.contact.phone_number ### text qoysak ham ham boladi
#     update.message.reply_text(text=f"Sizning xabaringiz: '{message}'")
#
#
#
# def contact_handler(update, context):
#     print(update.message.contact)
#     phone_number=update.message.contact   ### bu funksiya contactni olish uchun kerak
#     update.message.reply_text(text=f"Sizning nomiriz '{phone_number}'")
#
#
#
# def location_handler(update, context):
#     print(update.message.location)
#     location=update.message.location
#     update.message.reply_location(latitude=location.latitude, longitude=location.longutide) ## bu locatsiya uchun
#
#
# def main():
#     updater=Updater("1828443311:AAFC_9GaPz03an-SZrGpaBWsaONDmJt9xzM")    #### 1 -holat
#     dispatcher=updater.dispatcher
#
#
#     dispatcher.add_handler(CommandHandler("start", start_command))
#     dispatcher.add_handler(CommandHandler("menu", show_menu))               #### yerga esa yangi funksiya qoshsak shu yerga yozamz
#     dispatcher.add_handler(MessageHandler(Filters.text, message_handler))  ### text orniga command ham bersak boladi
#     dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler)) ###  bu qism cont olish uchun
#     dispatcher.add_handler(MessageHandler(Filters.location, location_handler)) ## bu bilan manzilni aniqlab olamz
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == '__main__':
    #main()