# from distutils.cmd import Command
import pandas as pd
import re as r
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,Message
from geopy.geocoders import Nominatim
import json

from loader import dp




def get_location_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    button = InlineKeyboardButton("Get nearby hotspots", request_location=True)
    keyboard.add(button)
    return keyboard


def get_contact_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = InlineKeyboardButton("Give Permission", request_contact=True)
    keyboard.add(button)
    return keyboard




def Start_query_key():
    button1 = KeyboardButton(text="🍺🏈 Stifler", callback_data="packed")
    button2 = KeyboardButton(text="🍸✨ Jim Halpert", callback_data="busy")
    button3 = KeyboardButton(text="🍾💎 50 Cent", callback_data="calm")
    # button2 = InlineKeyboardButton(text=" 🙅‍♂️ N0", callback_data="no_i_am_not_interested")
    keyboard_inline = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button1,button2).add(button3)
    return keyboard_inline


def crowd_keyboard():
    button1 = KeyboardButton(text="🔥packed", callback_data="packed")
    button2 = KeyboardButton(text="🔆busy", callback_data="busy")
    button3 = KeyboardButton(text="🌀calm", callback_data="calm")
    # button2 = InlineKeyboardButton(text=" 🙅‍♂️ N0", callback_data="no_i_am_not_interested")
    keyboard_inline = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button1,button2,button3)
    return keyboard_inline

def distance_keyboard():
    button1 = KeyboardButton(text="🚶walkable")
    button2 = KeyboardButton(text="🚕nearby")
    button3 = KeyboardButton(text="🚌far")
    # button2 = InlineKeyboardButton(text=" 🙅‍♂️ N0", callback_data="no_i_am_not_interested")
    keyboard_inline = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button1,button2,button3)
    return keyboard_inline
def price_keyboard():
    button1 = KeyboardButton(text="🪙budget")
    button2 = KeyboardButton(text="💵average")
    button3 = KeyboardButton(text="💰expensive")
    button4 = KeyboardButton(text="💎vip")
    # button2 = InlineKeyboardButton(text=" 🙅‍♂️ N0", callback_data="no_i_am_not_interested")
    keyboard_inline = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button1,button2).add(button3,button4)
    return keyboard_inline

    
def rating_keyboard():
    button1 = KeyboardButton(text="🌟certified")
    button2 = KeyboardButton(text="⭐underdogs")

    # button2 = InlineKeyboardButton(text=" 🙅‍♂️ N0", callback_data="no_i_am_not_interested")
    keyboard_inline = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button1,button2)
    return keyboard_inline


def scouter_keyboard():
    button1 = KeyboardButton(text="Top Experienced")
    # button2 = KeyboardButton(text="⭐underdogs")

    # button2 = InlineKeyboardButton(text=" 🙅‍♂️ N0", callback_data="no_i_am_not_interested")
    keyboard_inline = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button1)
    return keyboard_inline


