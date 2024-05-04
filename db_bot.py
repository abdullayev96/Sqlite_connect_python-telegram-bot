from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import sqlite3 as sq
from db_bot1 import *


(CHOOSING_LOCATION, CHOOSING_BOX, RATING_SERVICE) = range(3)


def start(update, context):
          reply_keyboard = [['Abdullayev B', 'Location B', 'Location C']]
          update.message.reply_text(text="Enter First name ",
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
          )
          context.user_data['state'] = CHOOSING_LOCATION


def received_message(update,  context):
          state = context.user_data.get('state')
          data = context.user_data


          if state == CHOOSING_LOCATION:
                    context.user_data['first_name'] = update.message.text
                    reply_keyboard = [['Box 1', 'Box 2', 'Box 3']]
                    update.message.reply_text(
                              'Please choose a box:',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               one_time_keyboard=True, resize_keyboard=True)
                    )
                    context.user_data['state'] = CHOOSING_BOX

                    print(context.user_data)

          elif state == CHOOSING_BOX:
                    context.user_data['last_name'] = update.message.text
                    reply_keyboard = [['Good', 'Average', 'Poor']]
                    update.message.reply_text(
                              'How was the employee treatment?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               one_time_keyboard=True, resize_keyboard=True)
                    )
                    context.user_data['state'] = RATING_SERVICE
                    print(context.user_data)


          elif state == RATING_SERVICE:
                    context.user_data['age'] = update.message.text
                    save_to_database(context.user_data)
                    print(context.user_data)


                    update.message.reply_text('Thank you for your feedback!', reply_markup=ReplyKeyboardRemove())
                    context.user_data.clear()

#
#
# def save_to_database(data):
#     try:
#         with sq.connect('base.db') as conn:
#             cur = conn.cursor()
#
#             cur.execute("""
#                 INSERT INTO user(first_name, last_name, age)
#                 VALUES (?, ?, ?)""",
#                 (data['first_name'], data['last_name'], data['age']))
#             conn.commit()
#     except sq.Error as e:
#         print(f"An error occurred: {e}")
#     finally:
#         if conn:
#             conn.close()
#



Token  = "6165627762:AAFG33CG1lKCXCjweahKcFcMwDpJ-XMB6Rw"

updater = Updater(Token)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, received_message))

updater.start_polling()
updater.idle()


