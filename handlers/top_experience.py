from aiogram import Bot, Dispatcher, executor, types
from keyboards import distance_keyboard
from loader import dp
import pandas as pd 
@dp.message_handler(text=['Top Experienced'])
async def welcome(message: types.Message):
    a = pd.read_csv("a.csv")
    if message.text =='Top Experienced':
        rows=[]
        # try:
        aa = 0
        print("hi i am top exp")
        for i, raw in a.sort_values("Rating_n", ascending=True).iterrows():
            raw = [raw["Place_name"], raw["Busy_hour"], raw["Rating_n"],
                raw['distance'], raw['place_url'], raw["price_range"], raw["rating"]]
            if (raw[5]) =="$$$$" or (raw[5]) =="$$$" and float(raw[6]) >float(4) and raw[1]>=70:
                print(raw)
                rows.append(raw)
        p_name=[]
        b_hours=[]
        r_numbar=[]
        
        distance=[]
        p_url=[]
        p_range=[]
        rating=[]
        for i in rows:
            try:
                p_name.append(i[0])
            except:
                p_name.append("")
            try:
                b_hours.append(i[1])
            except:
                b_hours.append("")
            try:
                r_numbar.append(i[2])
            except:
                r_numbar.append("")
            try:
                distance.append(i[3])
            except:
                distance.append("")
            try:
                p_url.append(i[4])
            except:
                p_url.append("")
            try:
                p_range.append(i[5])
            except:
                p_range.append("")
            try:
                rating.append(i[6])
            except:
                rating.append("")
        df_final1=pd.DataFrame({
        "Place_name":p_name,
        "Busy_hour":b_hours,
        "Rating_n":r_numbar,
        "distance":distance,
        "place_url":p_url,
        "price_range":p_range,
        "rating":rating,
        # "search_url":search_url
        })
        print(df_final1)
        for i, raw in df_final1.sort_values("distance", ascending=True).iterrows():
            raw = [raw["Place_name"], raw["Busy_hour"], raw["Rating_n"],
                raw['distance'], raw['place_url'], raw["price_range"], raw["rating"]]
            aa = aa+1
            if aa == 1:
                await message.answer("Here are a list of Top Experienced hotspots. ")
            Crowd = ""
            try:
                if raw[1] > 80:
                    Crowd = ' 🔥packed'
                elif 40 < raw[1] < 80:
                    Crowd = ' 🔆busy'
                elif 1 < raw[1] < 40:
                    Crowd = ' 🌀calm'
                elif raw[1] == 0:
                    Crowd = ' 🔒closed'
            except Exception as e:
                print(e)
                Crowd = ""
            try:
                if raw[5] == '$':
                    Price = '  🪙budget'
                elif raw[5] == "$$":
                    Price = ' 💵average'
                elif raw[5] == "$$$":
                    Price = ' 💰expensive'
                elif raw[1] == "$$$$":
                    Price = ' 💎vip'

            except:
                Price = raw[5]

            if Crowd == "":

                reply = f'''#.{aa}: {raw[0]}\nRating: ⭐ {raw[2]}\nDistance : 📍 {raw[3]}\nPrice : {Price} \n\n{raw[4]}'''
            else:
                reply = f'''#.{aa}:  {raw[0]}\nCrowd :  {Crowd}\nRating : ⭐ {raw[2]}\nDistance :  📍 {raw[3]}\nPrice : {Price} \n\n{raw[4]}'''
            await message.answer(reply)

            if aa > 4:
                break
    # except:
    #     await message.answer("Some technical issue occurs plz try again later")
    # await message.answer("If you would like to fully customize your nightlife experience please feel free to use the commands below 👇")   





