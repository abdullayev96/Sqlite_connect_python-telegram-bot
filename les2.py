# from telegram.ext import Updater, CommandHandler
# from telegram import BotCommand
#
#
# def start_command(update, context):
#     print(update.message)          #### 2 holat
#     print(update.message.from_user.id)   ### bu userni malumotlarini chiqarib beradi
#     commands=[
#         BotCommand(command="start", description="start knopkasini bosing"),  ## bular bilan  / qoyib chiqadigan qilsak boladi
#         BotCommand(command="help", description=" help knopkasini bosing"),
#         BotCommand(command="info", description="info knopkasini bosing"),
#         BotCommand(command="setting", description="setting knopkasini bosing"),
#     ]
#     context.bot.set_my_commands(commands=commands)
#     update.message.reply_text(                           #### 2 chi holat yerga funksiyalarni yozib
#         text="HTML:<b>Hello bro</b>, <i>Italic</i> <code>Code</> <s>100$</s> 97$ ",    ### bu yerga html kodlarini yozsak boladi
#         parse_mode="HTML"
#     )
#     update.message.reply_text(
#         text="MARKDOWN: **Good**",
#         perse_mode="MARKDOWN"
#     )
#
#     #context.bot.send_message(chat_id='614916220', text='jimsz  nima qilyapsz qaramisz 😡😡😡🐣🐣🐣!!!') ##bu bilan chat_id ga xabar yuboramz
#
#
# # def help_command(update, context):
# #     update.message.reply_text(text="siz/help commandani bosdingz")
# #     context.bot.send_message(chat_id="614916220", text="qanday yordam kerak szga ")
#
# def main():
#     updater=Updater("5062050502:AAFFhIegfMjLVa6uekT0cnb0sI1XZ4DyqcE")   ## 1 token beraladi
#     dispatcher=updater.dispatcher
#
#     dispatcher.add_handler(CommandHandler('start', start_command))
#
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__== '__main__':
#     main()

from telegram.ext import Updater, CommandHandler
from telegram import BotCommand



TOKEN = "5829432169:AAEfPZ9cC1367HyMTIYyyCGZziLxn0EmZpM"





def start_command(update, context):
    commands=[
        BotCommand(command="start", description="start knopkasini bosing"),
        BotCommand(command="help", description=" help knopkasini bosing"),
        BotCommand(command="info", description="info knopkasini bosing"),
        BotCommand(command="setting", description="setting knopkasini bosing"),
    ]
    context.bot.set_my_commands(commands=commands)


    # update.message.reply_text(
    #     text="HTML:<b>Hello bro</b>",   #### <i>Italic</i> <code>Code</> <s>100$</s> 97$
    #     parse_mode="HTML"
    # )
    # update.message.reply_text(
    #     text="MARKDOWN: **Good**",
    #     perse_mode="MARKDOWN"
    # )



def begin_func(update, context):
    user = update.message.from_user.first_name
    update.message.reply_text(text=f"Assalamu alaykum \n {user}  hush kelibsiz")

#


updater = Updater(TOKEN)
dispatcher  =  updater.dispatcher


dispatcher.add_handler(CommandHandler('start', begin_func))


updater.start_polling()

