from loader import dp

from aiogram import Bot, Dispatcher, executor, types
# from keyboards.crowd_key import crowd_keyboard
from loader import dp
import pandas as pd 

@dp.message_handler(commands=['scouter'])
async def welcome(message: types.Message):
        a = pd.read_csv("a.csv")
        try:

            aa = 0
            for i, raw in a.sort_values("distance", ascending=True).iterrows():
                raw = [raw["Place_name"], raw["Busy_hour"], raw["Rating_n"],
                    raw['distance'], raw['place_url'], raw["price_range"], raw["rating"]]
                try:
                    
                        aa = aa+1
                        if aa == 1:
                            await message.answer("Here are a list of ✨Popular hotspots. ")
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
                except:
                        pass
            if aa == 0:
                    await message.answer("No ✨Popular places found")
                # await message.answer("Here is a pro tip. If you are going alone as a stag, you might want to get there earlier. You may use the options below to narrow down your preferences", reply_markup=Filter_bord)
        except Exception as e:
            print(e)
            await message.answer("Some technical issue occurs plz try again later")
        await message.answer("If you would like to fully customize your nightlife experience please feel free to use the commands below 👇")   
