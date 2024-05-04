from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import BotCommand


TOKEN  = '6165627762:AAFpvknERznySUAyQ5441vBoDEzPdXKlICA'

updater = Updater(TOKEN)
dispatcher  =  updater.dispatcher

def start_handler(update, context):
    #update.message.reply_text(text="Yes or None")
    # commands  =  [
    #     BotCommand(command='start', description="sz start bosdngz "),
    #     BotCommand(command='help', description="sz help bosdngz "),
    #     BotCommand(command='menu', description="sz menu bosdngz "),
    #     BotCommand(command='settings', description="sz settings bosdngz "),
    # ]
    #context.bot.set_my_commands(commands=commands)

    commands = [
        BotCommand(command="start", description="Siz start commandasini bosdingz"),
        BotCommand(command="help", description="Siz help commandasini bosdingz"),
        BotCommand(command="settings", description="Siz settings commandasini bosdingz"),
        BotCommand(command="menu", description="Siz menu commandasini bosdingz")

    ]
    context.bot.set_my_commands(commands=commands)

    #update.message.reply_text(text="Hush kelibsz text kiriting !")
    # buttons  = [
    #     [KeyboardButton(text='Uzbek tili'), KeyboardButton(text="English")],
    #     [KeyboardButton(text='Arabic'), KeyboardButton(text="China")]
    # ]
    #
    # update.message.reply_text(
    #     text="Text yozing !",
    #     reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True, resize_keyboard=True)
    #
    #                           )
    # context.bot.send_message(update.message.chat_id, text='jimsz  nima qilyapsz qaramisz 😡😡😡😡👹👹👹👹🐣🐣🐣!!!')
    # context.bot.send_message(update.message.chat_id, text='yoq hech narsa')



dispatcher.add_handler(CommandHandler('start', start_handler))


updater.start_polling()





