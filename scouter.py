from loader import dp
import handlers
# from distutils.cmd import Command
from codecs import latin_1_decode
from ctypes import resize
from email.charset import add_alias
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,Message
from geopy.geocoders import Nominatim
import json
import re as r
import requests as re
import pandas as pd
from datetime import datetime
import pytz
from geopy.geocoders import Nominatim
# from random import randint
all_numbers=[]




@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text != '':
        rule = r.compile(r'(^[+0-9]{1,3})*([0-9]{10,11}$)')

        if rule.search(message.text):
            msg = "Phone number submitted successfully"
            all_numbers.append(message.text)
            await message.answer(msg)
        else:
            await message.answer("Hi there! Your AI wingman for everything nightlife. Click 👉 /start to begin  ")
    else:
        await message.reply(f"Your message is: {message.text}")

executor.start_polling(dp, skip_updates=False)