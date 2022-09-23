
from aiogram import Bot, Dispatcher, executor, types
from loader import dp
from functions import get_keyboard
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    print("hiii scouter")
    print(message)
    await message.answer("I can find the most packed spots near you. For this i need your current location", reply_markup=get_keyboard())


