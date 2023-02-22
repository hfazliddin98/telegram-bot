from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    buttons = [
        [
            InlineKeyboardButton('Talaba ma`lumoti', callback_data='malumot1'),
            InlineKeyboardButton('Talaba login', callback_data='malumot2'),
        ],
        [
            InlineKeyboardButton('Talaba dars jadvali', callback_data='malumot3'),
            InlineKeyboardButton('Talaba malumotini yangilash', callback_data='malumot4'),
        ]
    ]
    await update.message.reply_html('Asalomu Alaykum {}\n \n sizga qanday yordam bera olaman!!!'.format(user.first_name), 
                                    reply_markup=InlineKeyboardMarkup(buttons))
    


    


app = ApplicationBuilder().token("6108809609:AAHao6tTlZR3f_vaKLTxmiL1cqaqstyaSq8").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()