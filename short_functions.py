from loader import dp
import pandas as pd

from aiogram import Bot, Dispatcher, executor, types
def croud_busy_tags(raw):
                # aa=aa+1
                try:
                    if raw[1]>80:
                        Crowd=' 🔥 packed'
                    elif 40<raw[1]<80:
                        Crowd=' 🔆busy'
                    elif 1<raw[1]<40:
                        Crowd=' 🌀 calm'
                    elif raw[1]==0:
                        Crowd=' 🔒 closed'
                except Exception as e:
                    print(e)
                    Crowd=""
                try:
                    if raw[5]=='$':
                        Price='  🪙 budget'
                    elif raw[5] =="$$":
                        Price=' 💵 average'
                    elif raw[5]=="$$$":
                        Price=' 💰 expensive'
                    elif raw[1]=="$$$$":
                        Price=' 💎 vip'
                except:
                    Price=raw[5]
                return str(Crowd +"+"+Price)
            