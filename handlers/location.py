# from tkinter import Variable
from aiogram import Bot, Dispatcher, executor, types
from inline import inline_key
from loader import dp
from functions import get_data
import pandas as pd

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
    print(lat)
    print(lon)
    # initialize Nominatim API
    await message.answer("Please wait a few moments while I scout your places. I will send a message when completed.",reply_markup=types.ReplyKeyboardRemove())
    a=get_data(lat, lon)
    a.to_csv("a.csv")
    fgooglePlaceName=[]
    fbusy_index=[]
    fRating_n=[]
    fdistance=[]
    fplaceurl=[]
    fplat=[]
    fplong=[]
    fRating=[]
    fPriceRange=[]
    print("hi")
    for i ,raw in a.sort_values("Busy_hour",ascending=False).iterrows():
        raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
        # if intraw[1]>=90:
        fgooglePlaceName.append(raw[0])
        fdistance.append(raw[4])
        fbusy_index.append(raw[1])
        fRating_n.append(raw[2])
        fplaceurl.append(raw[3])
        # fplat.append(raw[4])
        # fplong.append(raw[5])
        fPriceRange.append(raw[5])
        fRating.append(raw[6])
    df_final=pd.DataFrame({
        "Place_name":fgooglePlaceName,
        "Busy_hour":fbusy_index,
        "Rating_n":fRating_n,
        "place_url":fplaceurl,
        "price_range":fPriceRange,
        "rating":fRating,
        "distance":fdistance
    })

    # try:
    if len(a)==0:
        # button1 = InlineKeyboardButton(text="😃 Yes", callback_data="yes_show_lit")
        # button2 = InlineKeyboardButton(text=" 🙅‍♂️ N0", callback_data="no_i_am_not_interested")
        # keyboard_inline = InlineKeyboardMarkup().add(button1, button2)
        await message.answer("there seems to be no places that are super lit tonight. ")
    else:
        no=10
        if len(df_final)<10:
            no=len(df_final)
        await message.answer(f" Here are the most packed places in the next few hours:")
        aa=0
        for i ,raw in df_final.iterrows():
            try:
                rr=int(raw["Busy_hour"])
            except:
                rr=0
            raw=[raw["Place_name"],rr,raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
            try:
                aa=aa+1
                try:
                    if raw[1]>80:
                        Crowd=' 🔥packed'+f"({raw[1]})"
                    elif 40<raw[1]<80:
                        Crowd=' 🔆busy'+f"({raw[1]})"
                    elif 1<raw[1]<40:
                        Crowd=' 🌀calm'+f"({raw[1]})"
                    elif raw[1]==0:
                        Crowd=' 🔒closed'+f"({raw[1]})"
                except Exception as e:
                    print(e)
                    Crowd=""
                try:
                    if raw[5]=='$':
                        Price='  🪙budget'
                    elif raw[5] =="$$":
                        Price=' 💵average'
                    elif raw[5]=="$$$":
                        Price=' 💰expensive'
                    elif raw[1]=="$$$$":
                        Price=' 💎vip'
                
                except:
                    Price=raw[5]

                if Crowd=="":

                    reply=f'''#.{aa}: {raw[0]}\nRating: ⭐ {raw[2]}\nDistance : 📍 {raw[4]}\nPrice : {Price} \n\n{raw[3]}'''
                else: 
                    reply=f'''#.{aa}:  {raw[0]}\nCrowd :  {Crowd}\nRating : ⭐ {raw[2]}\nDistance :  📍 {raw[4]}\nPrice : {Price} \n\n{raw[3]}'''
                await message.answer(reply)

                if aa>4:
                    break
            except Exception as e:
                print(e)
                print(raw)
                pass
        await message.answer("Here are some other popular options for finding your nightlife:",reply_markup=inline_key())
        await message.answer("If you would like to fully customize your nightlife experience please feel free to use the commands below 👇")   

    # except Exception as e:
    #     print(e)
    #     await message.answer("Some technical issue occurs plz try again later") 

