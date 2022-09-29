from aiogram import Bot, Dispatcher, executor, types
from inline import inline_key
from loader import dp
from loader import bot
# from aiogram import 
import json
import pandas as pd

from main_functions import get_data
from short_functions import croud_busy_tags

@dp.callback_query_handler(text=["stifler","jim_halpert","50_Cent"])
async def random_value(call: types.CallbackQuery):
    print(call)
    f=open("location.txt")
    for i in f.readlines():
        print(i)
        lat=float(i.split("+")[0])
        lon=float(i.split("+")[-1])
    
    if call.data == "stifler"  :
            print("hii Stifler")
            print(call.id)
            # aaaaa=bot.send_animation("./data.txt")
            ani=open("static/Stifler.mp4","rb")
            await call.message.answer_animation(animation=ani,reply_markup=types.ReplyKeyboardRemove())
            query="bars"
            a=get_data(lat, lon,query)
            username=str(call['from']['first_name']).replace("|","").replace("•","").replace("~","")
            print(username)
            a.to_csv(f"{username}.csv")
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
                fgooglePlaceName.append(raw[0])
                fdistance.append(raw[4])
                fbusy_index.append(raw[1])
                fRating_n.append(raw[2])
                fplaceurl.append(raw[3])
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
                await call.message.answer("there seems to be no places that are super lit tonight. ")
            else:
                no=10
                if len(df_final)<10:
                    no=len(df_final)
                aa=0
                for i ,raw in df_final.iterrows():
                    try:
                        rr=int(raw["Busy_hour"])
                    except:
                        rr=0
                    raw=[raw["Place_name"],rr,raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                # try:
                    
                    if raw[1]>=70 and raw[5]=="$":
                        aa=aa+1
                        ss=croud_busy_tags(raw)
                        Crowd=ss.split("+")[0]
                        Price=ss.split("+")[-1]
                        if Crowd=="":

                            reply=f'''#.{aa}: {raw[0]}\nReviews: ⭐ {raw[2]}\nDistance : 📍 {raw[4]}\nPrice : {Price} \n\n{raw[3]}'''
                        else: 
                            reply=f'''#.{aa}:  {raw[0]}\nCrowd :  {Crowd}\nReviews : ⭐ {raw[2]}\nDistance :  📍 {raw[4]}\nPrice : {Price}  \n\n{raw[3]}'''
                        await call.message.answer(reply)

                        if aa>3:
                                break
                if aa == 0:
                        await call.message.answer("No  places found")
                        # except Exception as e:
                        #     print(e)
                        #     print(raw)
                        #     pass
                # await message.answer("Here are some other popular options for finding your nightlife:",reply_markup=inline_key())
                await call.message.answer("If you would like to fully customize your nightlife experience please feel free to use 👇 the commands below")   
    elif call.data == "jim_halpert" :
            print("hii jim_halpert")
            ani=open("static/Jim.mp4","rb")
            await call.message.answer_animation(animation=ani,reply_markup=types.ReplyKeyboardRemove())
            query="nightlife"
            a=get_data(lat, lon,query)
            username=str(call['from']['first_name']).replace("|","").replace("•","").replace("~","")
            print(username)
            a.to_csv(f"{username}.csv")
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
            for i ,raw in a.sort_values("Rating_n",ascending=False).iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                fgooglePlaceName.append(raw[0])
                fdistance.append(raw[4])
                fbusy_index.append(raw[1])
                fRating_n.append(raw[2])
                fplaceurl.append(raw[3])
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
                await call.message.answer("there seems to be no places that are super lit tonight. ")
            else:
                no=10
                if len(df_final)<10:
                    no=len(df_final)
                # await message.answer(f" Here are the most packed places in the next few hours:")
                aa=0
                for i ,raw in df_final.iterrows():
                    try:
                        rr=int(raw["Busy_hour"])
                    except:
                        rr=0
                    raw=[raw["Place_name"],rr,raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                # try:
                    
                    if raw[1]>=70 and (raw[5]=="$$" or raw[5]=="$$$") and float(raw[6])>=float(4.0):
                        aa=aa+1
                        ss=croud_busy_tags(raw)
                        Crowd=ss.split("+")[0]
                        Price=ss.split("+")[-1]
                        if Crowd=="":

                            reply=f'''#.{aa}: {raw[0]}\nReviews: ⭐ {raw[2]}\nDistance : 📍 {raw[4]}\nPrice : {Price} \n\n{raw[3]}'''
                        else: 
                            reply=f'''#.{aa}:  {raw[0]}\nCrowd :  {Crowd}\nReviews : ⭐ {raw[2]}\nDistance :  📍 {raw[4]}\nPrice : {Price}  \n\n{raw[3]}'''
                        await call.message.answer(reply)

                        if aa>3:
                                break
                if aa == 0:
                        await call.message.answer("No  places found")
                        # except Exception as e:
                        #     print(e)
                        #     print(raw)
                        #     pass
                # await message.answer("Here are some other popular options for finding your nightlife:",reply_markup=inline_key())
                await call.message.answer("If you would like to fully customize your nightlife experience please feel free to use 👇 the commands below")   
        
    elif call.data == "50_Cent":
            print("hii 50_Cent")
            ani=open("static/50_cent.mp4","rb")
            await call.message.answer_animation(animation=ani,reply_markup=types.ReplyKeyboardRemove())
            query="nightlife"
            a=get_data(lat, lon,query)
            username=str(call['from']['first_name']).replace("|","").replace("•","").replace("~","")
            print(username)
            a.to_csv(f"{username}.csv")
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
            for i ,raw in a.sort_values("Rating_n",ascending=False).iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                fgooglePlaceName.append(raw[0])
                fdistance.append(raw[4])
                fbusy_index.append(raw[1])
                fRating_n.append(raw[2])
                fplaceurl.append(raw[3])
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
                await call.message.answer("there seems to be no places that are super lit tonight. ")
            else:
                no=10
                if len(df_final)<10:
                    no=len(df_final)
                # await message.answer(f" Here are the most packed places in the next few hours:")
                aa=0
                for i ,raw in df_final.iterrows():
                    try:
                        rr=int(raw["Busy_hour"])
                    except:
                        rr=0
                    raw=[raw["Place_name"],rr,raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                # try:
                    
                    if raw[5]=="$$$" or raw[5]=="$$$$" or raw[5] == "$$$$$":
                        aa=aa+1
                        ss=croud_busy_tags(raw)
                        Crowd=ss.split("+")[0]
                        Price=ss.split("+")[-1]
                        if Crowd=="":

                            reply=f'''#.{aa}: {raw[0]}\nReviews: ⭐ {raw[2]}\nDistance : 📍 {raw[4]}\nPrice : {Price} \n\n{raw[3]}'''
                        else: 
                            reply=f'''#.{aa}:  {raw[0]}\nCrowd :  {Crowd}\nReviews : ⭐ {raw[2]}\nDistance :  📍 {raw[4]}\nPrice : {Price}  \n\n{raw[3]}'''
                        await call.message.answer(reply)

                        if aa>3:
                                break
                if aa == 0:
                        await call.message.answer("No  places found")
                        # except Exception as e:
                        #     print(e)
                        #     print(raw)
                        #     pass
                # await message.answer("Here are some other popular options for finding your nightlife:",reply_markup=inline_key())
                await call.message.answer("If you would like to fully customize your nightlife experience please feel free to use 👇 the commands below")   
        
        
        
        
@dp.message_handler(text=['🍺🏈 Stifler',"🍸✨ Jim Halpert","🍾💎 50 Cent"])
async def kb_answer(message: types.Message):
    f=open("location.txt")
    for i in f.readlines():
        print(i)
        lat=float(i.split("+")[0])
        lon=float(i.split("+")[-1])
    if message.text=="🍺🏈 Stifler":
        print("hii Stifler")
        ani=open("static/Stifler.mp4","rb")
        await message.answer_animation(animation=ani,reply_markup=types.ReplyKeyboardRemove())
        query="bars"
        a=get_data(lat, lon,query)
        username=str(message['from']['first_name']).replace("|","").replace("•","").replace("~","")
        print(username)
        a.to_csv(f"{username}.csv")
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
            fgooglePlaceName.append(raw[0])
            fdistance.append(raw[4])
            fbusy_index.append(raw[1])
            fRating_n.append(raw[2])
            fplaceurl.append(raw[3])
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
            await message.answer("there seems to be no places that are super lit tonight. ")
        else:
            no=10
            if len(df_final)<10:
                no=len(df_final)
            aa=0
            for i ,raw in df_final.iterrows():
                try:
                    rr=int(raw["Busy_hour"])
                except:
                    rr=0
                raw=[raw["Place_name"],rr,raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
            # try:
                
                if raw[1]>=70 and raw[5]=="$":
                    aa=aa+1
                    ss=croud_busy_tags(raw)
                    Crowd=ss.split("+")[0]
                    Price=ss.split("+")[-1]
                    if Crowd=="":

                        reply=f'''#.{aa}: {raw[0]}\nReviews: ⭐ {raw[2]}\nDistance : 📍 {raw[4]}\nPrice : {Price} \n\n{raw[3]}'''
                    else: 
                        reply=f'''#.{aa}:  {raw[0]}\nCrowd :  {Crowd}\nReviews : ⭐ {raw[2]}\nDistance :  📍 {raw[4]}\nPrice : {Price}  \n\n{raw[3]}'''
                    await message.answer(reply)

                    if aa>3:
                            break
            if aa == 0:
                        await message.answer("No  places found")
                    # except Exception as e:
                    #     print(e)
                    #     print(raw)
                    #     pass
            # await message.answer("Here are some other popular options for finding your nightlife:",reply_markup=inline_key())
            await message.answer("If you would like to fully customize your nightlife experience please feel free to use 👇 the commands below")   



    elif message.text == "🍸✨ Jim Halpert":
            print("hii jim_halpert")
            ani=open("static/Jim.mp4","rb")
            await message.answer_animation(animation=ani,reply_markup=types.ReplyKeyboardRemove())
            query="nightlife"
            a=get_data(lat, lon,query)
            username=str(message['from']['first_name']).replace("|","").replace("•","").replace("~","")
            print(username)
            a.to_csv(f"{username}.csv")
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
            for i ,raw in a.sort_values("Rating_n",ascending=False).iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                fgooglePlaceName.append(raw[0])
                fdistance.append(raw[4])
                fbusy_index.append(raw[1])
                fRating_n.append(raw[2])
                fplaceurl.append(raw[3])
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
                await message.answer("there seems to be no places that are super lit tonight. ")
            else:
                no=10
                if len(df_final)<10:
                    no=len(df_final)
                # await message.answer(f" Here are the most packed places in the next few hours:")
                aa=0
                for i ,raw in df_final.iterrows():
                    try:
                        rr=int(raw["Busy_hour"])
                    except:
                        rr=0
                    raw=[raw["Place_name"],rr,raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                # try:
                    
                    if raw[1]>=70 and (raw[5]=="$$" or raw[5]=="$$$") and float(raw[6])>=float(4.0):
                        aa=aa+1
                        ss=croud_busy_tags(raw)
                        Crowd=ss.split("+")[0]
                        Price=ss.split("+")[-1]
                        if Crowd=="":

                            reply=f'''#.{aa}: {raw[0]}\nReviews: ⭐ {raw[2]}\nDistance : 📍 {raw[4]}\nPrice : {Price} \n\n{raw[3]}'''
                        else: 
                            reply=f'''#.{aa}:  {raw[0]}\nCrowd :  {Crowd}\nReviews : ⭐ {raw[2]}\nDistance :  📍 {raw[4]}\nPrice : {Price}  \n\n{raw[3]}'''
                        await message.answer(reply)

                        if aa>3:
                                break
                if aa == 0:
                    await message.answer("No  places found")
                        # except Exception as e:
                        #     print(e)
                        #     print(raw)
                        #     pass
                # await message.answer("Here are some other popular options for finding your nightlife:",reply_markup=inline_key())
                await message.answer("If you would like to fully customize your nightlife experience please feel free to use 👇 the commands below")   
    elif message.text == "🍾💎 50 Cent":
            print("hii 50_Cent")
            ani=open("static/50_cent.mp4","rb")
            await message.answer_animation(animation=ani,reply_markup=types.ReplyKeyboardRemove())
            query="nightlife"
            a=get_data(lat, lon,query)
            username=str(message['from']['first_name']).replace("|","").replace("•","").replace("~","")
            print(username)
            a.to_csv(f"{username}.csv")
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
            for i ,raw in a.sort_values("Rating_n",ascending=False).iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                fgooglePlaceName.append(raw[0])
                fdistance.append(raw[4])
                fbusy_index.append(raw[1])
                fRating_n.append(raw[2])
                fplaceurl.append(raw[3])
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
                await message.answer("there seems to be no places that are super lit tonight. ")
            else:
                no=10
                if len(df_final)<10:
                    no=len(df_final)
                # await message.answer(f" Here are the most packed places in the next few hours:")
                aa=0
                for i ,raw in df_final.iterrows():
                    try:
                        rr=int(raw["Busy_hour"])
                    except:
                        rr=0
                    raw=[raw["Place_name"],rr,raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                    
                    if raw[5]=="$$$" or raw[5]=="$$$$" or raw[5] == "$$$$$":
                        aa=aa+1
                        ss=croud_busy_tags(raw)
                        Crowd=ss.split("+")[0]
                        Price=ss.split("+")[-1]
                        if Crowd=="":

                            reply=f'''#.{aa}: {raw[0]}\nReviews: ⭐ {raw[2]}\nDistance : 📍 {raw[4]}\nPrice : {Price} \n\n{raw[3]}'''
                        else: 
                            reply=f'''#.{aa}:  {raw[0]}\nCrowd :  {Crowd}\nReviews : ⭐ {raw[2]}\nDistance :  📍 {raw[4]}\nPrice : {Price}  \n\n{raw[3]}'''
                        await message.answer(reply)

                        if aa>3:
                                break
                if aa == 0:
                        await message.answer("No  places found")
                        # except Exception as e:
                        #     print(e)
                        #     print(raw)
                        #     pass
                # await message.answer("Here are some other popular options for finding your nightlife:",reply_markup=inline_key())
                await message.answer("If you would like to fully customize your nightlife experience please feel free to use 👇 the commands below")   
        
        
