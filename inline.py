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
    button1 = InlineKeyboardButton(text="Most reviewed bars nearby", callback_data="most_reviewed_nearby")
    # button2 = InlineKeyboardButton(text=" 🙅‍♂️ N0", callback_data="no_i_am_not_interested")
    keyboard_inline = InlineKeyboardMarkup().add(button1)
    return keyboard_inline