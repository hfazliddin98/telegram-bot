import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

API_TOKEN = '6381039530:AAEqs25byPNY7YCTV2_ed3TGAJdsUs7w_tk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

login_endpoint = "https://student.hemis.uz/rest/v1/auth/login"

jwt_token = "_HCnxPew6Lken00smp3bJOPBuQc3-HbA"
payload = {
    "login": 999211100073,
    "password": "DD7777777"
}
req = requests.post(login_endpoint, data=payload)
data = req.json()
user_token = data["data"]["token"]

login = KeyboardButton('Login')
parol = KeyboardButton('Parol alamshtirish')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(login).add(parol)

malumot = KeyboardButton('Talaba malumoti')
jadval = KeyboardButton('Talaba dars jadvali')
yangilash = KeyboardButton('Talaba malumotini yangilash')
asosiy = KeyboardButton('Asosiy sahifaga qaytish')
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(malumot,jadval).add(yangilash).add(asosiy)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   
    await message.reply("Asalomu alaykum sizga qanday yordam bera olaman", reply_markup=keyboard1)    



@dp.message_handler()
async def kirish(message: types.Message):
    if message.text == 'Login':        
        
        await message.answer('Sizga qanday yordam bera olaman', reply_markup=keyboard2) 
       
    
    elif message.text == 'Parol alamshtirish':        
        await message.answer(f'Talaba id kiriting ') 
        
       
    
    elif message.text == 'Asosiy sahifaga qaytish':
        await message.answer('Asoiy sahifaga qaytdi', reply_markup=keyboard1)  
    else:
        await message.answer(f'Sizning parolingiz {user_token}', reply_markup=keyboard1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

