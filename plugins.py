from pyrogram.types import bots_and_keyboards,InlineKeyboardMarkup,InlineKeyboardButton
from pyrogram.enums.message_entity_type import MessageEntityType
import random
from asyncio import sleep
from tracemalloc import Traceback




show_profile = 'pm1 test bot by **anti_bug**'
main_pm = 'pm2 test bot by **anti_bug**'
bot = 'MeloGapbot' # @MeloGapbot | @TeleChateBot




async def main_func(client,message,pm1,pm2,sleep_time): 
    if message.text is not None and 'به مخاطبت سلام کن 🗣' in message.text: 
            await sleep(sleep_time) 
            await message.reply(pm1,quote = False) 
            await message.reply(pm2,quote=False) 
            await sleep(10-sleep_time) 
            await message.reply('پایان چت',quote = False) 
    elif message.reply_markup and type(message.reply_markup) is bots_and_keyboards.inline_keyboard_markup.InlineKeyboardMarkup: 
            for x in message.reply_markup.inline_keyboard: 
                for i in range(len(list(x))): 
                    if '🎲 جستجوی شانسی' == x[i].text: 
                        await sleep(4)
                        try: 
                            await message.click(x[i].text) 
                        except Exception as e: 
                            pass 
                    elif '❌اتمام چت' == x[i].text: 
                        try: 
                            await message.click(x[i].text) 
                        except Exception as e: 
                            pass 
    elif message.text is not None and type(message.reply_markup) is bots_and_keyboards.reply_keyboard_markup.ReplyKeyboardMarkup: 
             
            keys = [] 
            for x in message.reply_markup.keyboard: 
                for i in x: 
                    keys.append(i) 
            if 'پایان چت' not in keys: 
                    await sleep(2) 
                    await client.send_message(message.from_user.id,'🔗 به یه ناشناس وصلم کن!')