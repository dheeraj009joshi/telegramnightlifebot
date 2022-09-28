# from tkinter import Variable
from base64 import encode
import json
from aiogram import Bot, Dispatcher, executor, types
from inline import inline_key
from keyboards import Start_query_key, get_location_keyboard
from loader import dp
from main_functions import get_data
import pandas as pd
all_users_last_querry={}
from geopy.geocoders import Nominatim
@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    global aa
    global a
    global Filter_bord
    global lat
    global lon
    lat = message.location.latitude
    lon = message.location.longitude
    u=open("location.txt","w")
    u.write(str(lat)+"+"+str(lon))
    print(lat)
    print(lon)
    f=open('all_users_details.json',encoding="utf-8")
    all_users_details = json.load(f)
    f.close()
    # print(all_users_details[message.chat.first_name]["location"]["lat"])

    print( all_users_details[message.chat.first_name]["location"])
    all_users_details[message.chat.first_name]["location"]={"lat":lat,"long":lon}
    # all_users_details[message.chat.first_name]["location"]["long"]=str(lon)

    print(all_users_details)
    js=open("all_users_details.json","w",encoding="utf-8")
    js.write(str(all_users_details).replace("'",'"'))
    js.close()
    await message.answer("Location Done",reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Select your vibe:",reply_markup=inline_key())
    await message.answer("Either select from the top or bottom",reply_markup=Start_query_key())
    

@dp.message_handler(content_types=['contact'])
async def handle_location(message: types.Message):
    print(message.contact.phone_number)
    try:
        f=open('all_users_details.json',encoding="utf-8")
        all_users_details = json.load(f)
        f.close()
    except:
        all_users_details={}
    all_users_details[message.chat.first_name]={"phoneno":f"+{message.contact.phone_number}","location":{}}
    js=open("all_users_details.json","w",encoding="utf-8")
    js.write(str(all_users_details).replace("'",'"'))
   
    # js.close()
    await message.answer("Contact added Successfully ",)
    await message.answer("Now Location",reply_markup=get_location_keyboard())
    