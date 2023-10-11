import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from states import Foydalanuvchi, salom, baza


TOKEN = "6381039530:AAEqs25byPNY7YCTV2_ed3TGAJdsUs7w_tk"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:    
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!\n"
                         f"Malumot olish uchun /malumotim ustiga bosing?")

try:
    @dp.message(Command('malumotim'))
    async def malumotlar(message: types.Message, state: FSMContext) -> None:    
    
        await message.answer('Familyangizni kiriting')
        await state.set_state(Foydalanuvchi.familya)        
        
    @dp.message(Foydalanuvchi.familya)
    async def familyalar(message: types.Message, state=FSMContext) -> None:
        familya = message.text
        await state.update_data({
            'familya':familya
        })
        await message.answer('Ismingizni kiriting')
        await state.set_state(Foydalanuvchi.ism)

    @dp.message(Foydalanuvchi.ism)
    async def ismlar(message: types.Message, state=FSMContext) -> None:
        ism = message.text        
        await state.update_data({
            'ism':ism
        })

        data = await state.get_data()
        fm = data['familya']
        im = data['ism']
        # await message.answer(f'Familyangiz-{fm}\n'
        #                      f'Ismingiz-{im}')

        await message.answer(salom(fm,im))        
        for dt in baza(fm,im): 
            try:        
            
                await message.answer(f'Imtihon kuni: {dt[0]}\n'
                                        f'Session id: {dt[3]}\n'
                                        f'Total score of the test: {dt[9]}\n'
                                        f'Speaking score: {dt[14]}')
            except:
                await message.answer('Bunda ma`lumot yoq')
        
        await state.clear()

except:
    @dp.message(CommandStart())
    async def command_start_handler(message: Message) -> None:    
        await message.answer(f"Hello, {hbold(message.from_user.full_name)}!\n"
                         f"Malumot olish uchun /malumotim ustiga bosing?")

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())