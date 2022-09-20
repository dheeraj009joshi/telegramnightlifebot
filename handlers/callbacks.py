from aiogram import Bot, Dispatcher, executor, types
from loader import dp
import json
import pandas as pd

@dp.callback_query_handler(text=["most_reviewed_nearby", "experience",  "underdogs", "certified" ,"expensive", "budget", "far", "nearby", "yes_show_lit", "yes_i_am_interested","no_i_am_not_interested","Las Vegas, Nevada","Bangalore, KA",'Atlanta, GA',"Mumbai, ","My City is Missing"])
async def random_value(call: types.CallbackQuery):
    global city 
    a = pd.read_csv("a.csv")
    if call.data == "yes_i_am_interested":
        global cities_button
       
    elif call.data == "nearby":
        try:
            
            aa=0
            for i ,raw in a.sort_values("distance").iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                if float(raw[3])<=5:
                    aa=aa+1
                    if aa==1:
                        await call.message.answer("Here are a list of nearby hotspots that are going to be super lit tonight.")
                    try:
                        reply=f"{raw[4]}\n\nNO.{aa}:- \nName of the place :- {raw[0]}\nBusy Hours :-- {raw[1]}\nRatingNumber:-- {raw[2]}\nDistance :-- {raw[3]}\nPriceRange :-- {raw[5]}\nRating :-- {('%.2f' % float(raw[6]))}"
                        await call.message.answer(reply)
                        if aa>4:
                            break
                    except:
                        print(raw)
                        pass
            if aa==0:   
                await call.message.answer("There is no near place found in around 5km, try for another ")
            await call.message.answer("Here is a pro tip. If you are going alone as a stag, you might want to get there earlier. You may use the options below to narrow down your preferences",reply_markup=Filter_bord)   
        except Exception as e:
            print(e)
            await call.message.answer("Some technical issue occurs plz try again later") 

    elif call.data == "far":
        try:

            aa=0
            for i ,raw in a.sort_values("distance",ascending=True).iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                if float(raw[3])<=15:
                    aa=aa+1
                    if aa==1:
                        await call.message.answer("Here are a list of far hotspots that are going to be super lit tonight.")
                    
                    try:
                        reply=f"{raw[4]}\n\nNO.{aa}:- \nName of the place :- {raw[0]}\nBusy Hours :-- {raw[1]}\nRatingNumber:-- {raw[2]}\nDistance :-- {raw[3]}\nPriceRange :-- {raw[5]}\nRating :-- {('%.2f' % float(raw[6]))}"
                        await call.message.answer(reply)
                        if aa>4:
                            break
                    except:
                        print(raw)
                        pass
            if aa==0: 
                await call.message.answer("NO place found in area of 15km try for another ")
            await call.message.answer("Here is a pro tip. If you are going alone as a stag, you might want to get there earlier. You may use the options below to narrow down your preferences",reply_markup=Filter_bord)   
        except Exception as e:
            print(e)
            await call.message.answer("Some technical issue occurs plz try again later") 

    elif call.data == "budget":
        try:
          
            aa=0
            for i ,raw in a.sort_values("distance", ascending=True).iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                if raw[5]!="$$$":
                    aa=aa+1
                    if aa==1:
                        await call.message.answer("Here are a list of budget hotspots that are going to be super lit tonight.")
                    
                    try:
                        reply=f"{raw[4]}\n\nNO.{aa}:- \nName of the place :- {raw[0]}\nBusy Hours :-- {raw[1]}\nRatingNumber:-- {raw[2]}\nDistance :-- {raw[3]}\nPriceRange :-- {raw[5]}\nRating :-- {('%.2f' % float(raw[6]))}"
                        await call.message.answer(reply)
                        if aa>4:
                            break
                    except:
                        print(raw)
                        pass
            if aa==0: 
                await call.message.answer("NO budget place found try for another ")
            # await call.message.answer("NO place found try for another in area of 15km")
            await call.message.answer("Here is a pro tip. If you are going alone as a stag, you might want to get there earlier. You may use the options below to narrow down your preferences",reply_markup=Filter_bord)   
        except Exception as e:
            print(e)
            await call.message.answer("Some technical issue occurs plz try again later") 

    elif call.data == "expensive":
        try:
            aa=0
            for i ,raw in a.sort_values("distance", ascending=True).iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                if raw[5]=="$$$" or raw[5]=="$$$$":
                    aa=aa+1
                    if aa==1:
                        await call.message.answer("Here are a list of expensive hotspots that are going to be super lit tonight.")
                    
                    try:
                        reply=f"{raw[4]}\n\nNO.{aa}:- \nName of the place :- {raw[0]}\nBusy Hours :-- {raw[1]}\nRatingNumber:-- {raw[2]}\nDistance :-- {raw[3]}\nPriceRange :-- {raw[5]}\nRating :-- {('%.2f' % float(raw[6]))}"
                        await call.message.answer(reply)
                        if aa>4:
                            break
                    except:
                        print(raw)
                        pass
            if aa==0: 
                await call.message.answer("NO expensive place found try for another ")
            # await call.message.answer("NO place found try for another in area of 15km")
            await call.message.answer("Here is a pro tip. If you are going alone as a stag, you might want to get there earlier. You may use the options below to narrow down your preferences",reply_markup=Filter_bord)   
        except Exception as e:
            print(e)
            await call.message.answer("Some technical issue occurs plz try again later") 

    elif call.data == "experience":
        try:
            
            aa=0
            for i ,raw in a.sort_values("Rating_n", ascending=False).iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                try:
                        reply=f"{raw[4]}\n\nNO.{aa}:- \nName of the place :- {raw[0]}\nBusy Hours :-- {raw[1]}\nRatingNumber:-- {raw[2]}\nDistance :-- {raw[3]}\nPriceRange :-- {raw[5]}\nRating :-- {('%.2f' % float(raw[6]))}"
                        await call.message.answer(reply)
                        if aa>4:
                            break
                        aa=aa+1
                except:
                    print(raw)
                    pass
            if aa==0: 
                await call.message.answer("NO experience place found try for another ")
            # await call.message.answer("NO place found try for another in area of 15km")
            await call.message.answer("Here is a pro tip. If you are going alone as a stag, you might want to get there earlier. You may use the options below to narrow down your preferences")   
        except Exception as e:
            print(e)
            await call.message.answer("Some technical issue occurs plz try again later") 

    elif call.data == "underdogs":
        try:
          
            aa=0
            for i ,raw in a.sort_values("rating", ascending=True).iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                if float(raw[6])<4:
                    aa=aa+1
                    if aa==1:
                        await call.message.answer("Here are a list of underdogs hotspots that are going to be super lit tonight.")
                    
                    try:
                        print("hiii undergoes")
                        reply=f"{raw[4]}\n\nNO.{aa}:- \nName of the place :- {raw[0]}\nBusy Hours :-- {raw[1]}\nRatingNumber:-- {raw[2]}\nDistance :-- {raw[3]}\nPriceRange :-- {raw[5]}\nRating :-- {('%.2f' % float(raw[6]))}"
                        await call.message.answer(reply)
                        if aa>4:
                            break
                    except:
                        print(raw)
                        pass
            if aa==0: 
                await call.message.answer("NO underdogs place found try for another ")
            await call.message.answer("Here is a pro tip. If you are going alone as a stag, you might want to get there earlier. You may use the options below to narrow down your preferences")   
        except Exception as e:
            print(e)
            await call.message.answer("Some technical issue occurs plz try again later") 

    elif call.data == "certified":
        print("entered")
        try:
           
            aa=0
            for i ,raw in a.sort_values("rating",ascending=False).iterrows():
                raw=[raw["Place_name"],raw["Busy_hour"],raw["Rating_n"],raw['distance'],raw['place_url'],raw["price_range"],raw["rating"]]
                if float(raw[6])>=float(4):
                    aa=aa+1
                    if aa==1:
                        await call.message.answer("Here are a list of certified hotspots that are going to be super lit tonight.")
                    try:
                        reply=f"{raw[4]}\n\nNO.{aa}:- \nName of the place :- {raw[0]}\nBusy Hours :-- {raw[1]}\nRatingNumber:-- {raw[2]}\nDistance :-- {raw[3]}\nPriceRange :-- {raw[5]}\nRating :-- {('%.2f' % float(raw[6]))}"
                        await call.message.answer(reply)
                        if aa>4:
                            break
                    except:
                        print(raw)
                        pass
            if aa==0: 
                await call.message.answer("NO certified place found try for another ")
            print("hiiiii  certified")
            # await call.message.answer("NO place found try for another in area of 15km")
            await call.message.answer("Here is a pro tip. If you are going alone as a stag, you might want to get there earlier. You may use the options below to narrow down your preferences")   
        except Exception as e:
            print(e)
            await call.message.answer("Some technical issue occurs plz try again later") 
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

                        reply=f'''#.{aa+1}: {raw[0]}\nRating: ⭐ {raw[2]}\nDistance : 📍 {raw[3]}\nPrice : {Price} \n\n{raw[4]}'''
                    else: 
                        reply=f'''#.{aa+1}:  {raw[0]}\nCrowd :  {Crowd}\nRating : ⭐ {raw[2]}\nDistance :  📍 {raw[3]}\nPrice : {Price} \n\n{raw[4]}'''
                    await call.message.answer(reply)
                    aa=aa+1
                    if aa>4:
                        break
                except Exception as e:
                    print(e)
                    print(raw)
                    pass
            if aa==0: 
                await call.message.answer("NO certified place found try for another ")
            print("hiiiii  certified")
            # await call.message.answer("NO place found try for another in area of 15km")
            await call.message.answer("Here is a pro tip. If you are going alone as a stag, you might want to get there earlier. You may use the options below to narrow down your preferences")   
        except Exception as e:
            print(e)
            await call.message.answer("Some technical issue occurs plz try again later") 
