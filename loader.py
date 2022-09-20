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
bot = Bot(token='5648147213:AAESRrpQ32vNGUx-I_Z9ZtfmlrWQ8VkB9dY') # TEST BOT
dp = Dispatcher(bot)

