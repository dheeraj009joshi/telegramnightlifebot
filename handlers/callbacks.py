from aiogram import Bot, Dispatcher, executor, types
from inline import inline_key
from loader import dp
import json
import pandas as pd

@dp.callback_query_handler(text=["live_hottest","most_reviewed_nearby"])
async def random_value(call: types.CallbackQuery):
    global city 
    a = pd.read_csv("a.csv")
    if call.data == "yes_i_am_interested":
        global cities_button
       
    
    elif call.data == "most_reviewed_nearby":
        print("most_reviewed_nearby")
        try:
           
            aa=0
            for i ,raw in a.sort_values("Rating_n",ascending=False).iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                if float(raw[6])>=float(4):
                    aa=aa+1
                    if aa==1:
                        await call.message.answer("Here are a list of most reviewed places.")
                try:
              
                    try:
                        if raw[1]>80:
                            Crowd=' 🔥packed'
                        elif 40<raw[1]<80:
                            Crowd=' 🔆busy'
                        elif 1<raw[1]<40:
                            Crowd=' 🌀calm'
                        elif raw[1]==0:
                            Crowd=' 🔒closed'
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

                        reply=f'''#.{aa}: {raw[0]}\nRating: ⭐ {raw[2]}\nDistance : 📍 {raw[3]}\nPrice : {Price} \n\n{raw[4]}'''
                    else: 
                        reply=f'''#.{aa}:  {raw[0]}\nCrowd :  {Crowd}\nRating : ⭐ {raw[2]}\nDistance :  📍 {raw[3]}\nPrice : {Price} \n\n{raw[4]}'''
                    await call.message.answer(reply)
 
                    if aa>4:
                        break
                except Exception as e:
                    print(e)
                    print(raw)
                    pass
            if aa==0: 
                await call.message.answer("NO certified place found try for another ")
            # print("hiiiii  certified")
            await call.message.answer("Here are some other popular options for finding your nightlife:",reply_markup=inline_key())
            # await call.message.answer("NO place found try for another in area of 15km")
            await call.message.answer("If you would like to fully customize your nightlife experience please feel free to use the commands below 👇")   
        except Exception as e:
            print(e)
            await call.message.answer("Some technical issue occurs plz try again later") 
    
    
    elif call.data == "live_hottest":
        print("live_hottest")
        try:
           
            aa=0
            for i ,raw in a.sort_values("Busy_hour",ascending=False).iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                if float(raw[6])>=float(4):
                    aa=aa+1
                    if aa==1:
                        await call.message.answer("Here are a list of most reviewed places.")
                try:
              
                    try:
                        if raw[1]>80:
                            Crowd=' 🔥packed'
                        elif 40<raw[1]<80:
                            Crowd=' 🔆busy'
                        elif 1<raw[1]<40:
                            Crowd=' 🌀calm'
                        elif raw[1]==0:
                            Crowd=' 🔒closed'
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

                        reply=f'''#.{aa}: {raw[0]}\nRating: ⭐ {raw[2]}\nDistance : 📍 {raw[3]}\nPrice : {Price} \n\n{raw[4]}'''
                    else: 
                        reply=f'''#.{aa}:  {raw[0]}\nCrowd :  {Crowd}\nRating : ⭐ {raw[2]}\nDistance :  📍 {raw[3]}\nPrice : {Price} \n\n{raw[4]}'''
                    await call.message.answer(reply)
                  
                    if aa>4:
                        break
                except Exception as e:
                    print(e)
                    print(raw)
                    pass
            if aa==0: 
                await call.message.answer("NO certified place found try for another ")
            # print("hiiiii  certified")
            await call.message.answer("Here are some other popular options for finding your nightlife:",reply_markup=inline_key())
            # await call.message.answer("NO place found try for another in area of 15km")
            await call.message.answer("If you would like to fully customize your nightlife experience please feel free to use the commands below 👇")   
        except Exception as e:
            print(e)
            await call.message.answer("Some technical issue occurs plz try again later") 
