# from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
# from telegram import ReplyKeyboardMarkup, KeyboardButton
#


# def start_command(update, context):
#     print(update.message)          #### 2 holat
#     print(update.message.from_user.id)   ### bu userni malumotlarini chiqarib beradi
#     update.message.reply_text(text=f" siz/ start commandasini bosdingz!!!")  #### 2 chi holat yerga funksiyalarni yozib
#     context.bot.send_message(chat_id='427345476', text=' nima qilyapsz qaramisz dars qiling tez😡😡😡😡👹👹👹👹🐣🐣🐣!!!') ##bu bilan chat_id ga xabar yuboramz
#
#
#
#
# def show_menu(update, context):    ##### 4 holat buttons ochamz
#     buttons=[
#         [KeyboardButton(text="Send your age ", request_contact=True), KeyboardButton(text="Send your habbi ", request_location=True)],
#         [KeyboardButton(text="send first_name"), KeyboardButton(text="send last_name")],
#
#     ]
#     update.message.reply_text(
#         text="Menu",                                                    ### one_time bu bir martalik knopkani korsatadi
#         reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True) ### resize_keyboard True bolsa knopkalar bir marta chiqadi
#     )
#
#
# def message_handler(update, context):
#     print(update.message.from_user)
#     message=update.message.text                  ###### 3 holat bu biror user start bossa oziga text qaytadi
#     update.message.reply_text(text=f" Sizning xabaringz '{message}' ")  # oziga yozganini qaytaradi
#
#
#
# def contact_handler(update, context):
#     print(update.message.contact)
#     phone_number=update.message.contact
#     #update.message.reply_text(text=f"sizni raqamz '{phone_number}'")
#
#
# def location_handler(update, context):
#     print(update.message.location)
#     location=update.message.location
#     #update.message.reply_location(latitude=location.latitude, longitude=location.longitude)
#
#
# def main():
#     updater=Updater("")   ## 1 token beraladi
#     dispatcher=updater.dispatcher
#
#     #dispatcher.add_handler(MessageHandler(Filters.command, start_command))
#     dispatcher.add_handler(CommandHandler('start', start_command))     ###### Filters.command buni bersak faqat startdan boshqa camandalar
#     dispatcher.add_handler(CommandHandler('menu', show_menu))
#     dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler)) #### command bolsa textlarni qaytarmidi
#     dispatcher.add_handler(MessageHandler(Filters.command, message_handler))
#     dispatcher.add_handler(MessageHandler(Filters.location, location_handler))
#
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__== '__main__':
#     main()
