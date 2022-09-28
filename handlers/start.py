
from aiogram import Bot, Dispatcher, executor, types
from keyboards import get_contact_keyboard
from loader import dp
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    print("hiii scouter")
    print(message)
    await message.answer("I can find the most packed spots near you. For this i need your current location", reply_markup=get_contact_keyboard())


