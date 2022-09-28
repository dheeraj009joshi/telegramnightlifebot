# from distutils.cmd import Command
from codecs import latin_1_decode
from ctypes import resize
from email.charset import add_alias
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,Message
from geopy.geocoders import Nominatim
import json


def inline_key():
    button1 = InlineKeyboardButton(text="🍺🏈 Stifler - Stand, cheer, and chug.", callback_data="stifler")
    button2 = InlineKeyboardButton(text="🍸✨ Jim Halpert - Sit, talk, and drink. ", callback_data="jim_halpert")
    button3 = InlineKeyboardButton(text=" 🍾💎 50 Cent - Dance, shout, and pop. ", callback_data="50_Cent")
    keyboard_inline = InlineKeyboardMarkup().add(button1).add(button2).add(button3)
    return keyboard_inline