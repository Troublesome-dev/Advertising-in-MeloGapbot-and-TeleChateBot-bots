from pyrogram import Client,filters,idle
from pyrogram.types import Message
from tracemalloc import Traceback
import plugins



bot = Client('session',api_id=123456789,api_hash='abcdefghijklmnopqrstuvwxyz:ABCDEFGHIGKLMNOPQRSTUVWXYZ')


bot.start()
bot.send_message(plugins.bot,'این ربات توسط **t.me/anti_bug** ساخته شده است')


#This bot is made by t.me/anti_bug

@bot.on_message(filters.chat(plugins.bot))
async def main(c:Client,m:Message):
    await plugins.main_func(client=c,message=m,pm1=plugins.show_profile,pm2=plugins.main_pm,sleep_time=2)
    
    
idle()
bot.stop()