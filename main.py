import logging, os, random
from pyrogram import filters, Client, __version__ as pyro
from pyrogram.types import *

import requests 

# enable logging
FORMAT = "[Truth-or-Dare] %(message)s"
logging.basicConfig(
    level=logging.INFO, format=FORMAT
)
  

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
SUPPORT = os.environ.get("SUPPORT", None)
UPDATES = os.environ.get("UPDATES", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None) 


bot = Client("nandhabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


buttons = [[
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"t.me/{BOT_USERNAME}?startgroup=true"),
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_back"),
           ],[
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT}"),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATES}")]]

PM_START_TEXT = """
**Welcome** {}~ kun 😈
`I'm A Truth or Dare Telegram Bot! `
**Make Your Groups Active By Adding Me There! ××**
"""

@bot.on_message(filters.command(["start","help"]))
async def start(_, m):
       url = "http://telegra.ph/file/c50b1959b61acf73f0a57.jpg"
       await m.reply_photo(photo=url,caption=PM_START_TEXT.format(m.from_user.mention),
             reply_markup=InlineKeyboardMarkup(buttons))
    
LANG_CODE = [[InlineKeyboardButton("Lang Codes!", callback_data="")]]
    
    
TRUTH_STRING = """ ~~ ** Hey! {} ~~**
{} give you a Truth! ~ 😳
~~ **Here the truth:~~ ** **{}** 😈
~~ **Now tell the truth to** ~~: **{}**! 😰
"""


@bot.on_message(filters.command("truth"))
async def truth(_, m):
       reply = m.reply_to_message
       name1 = reply.from_user.first_name
       name2 = m.from_user.first_name
       API = requests.get("https://api.truthordarebot.xyz/v1/truth").json()
       Bengali = API["translations"]["bn"]
       German = API["translations"]["de"]
       Spanish = API["translations"]["es"]
       French = API["translations"]["fr"]
       Hindi = API["translations"]["hi"]
       Tagalog = API["translations"]["tl"]
       Indonesian = API["translations"]["id"]
       if len(m.command) < 2:
             await m.reply_text("baka! read the langs codes!😑",
             reply_markup=InlineKeyboardMarkup(LANG_CODE))
             return
        text = m.text.split(None, 1)[1]
        if reply:
           if text.endswith("bn"):
               await m.reply_text(TRUTH_STRING.format(name1,name2,Bengali,name2)
               return
           if text.endswith("de"):
               await m.reply_text(TRUTH_STRING.format(name1,name2,German,name2)
               return
           if text.endswith("es"):
               await m.reply_text(TRUTH_STRING.format(name1,name2,Spanish,name2)
               
                                  
                                  
                                  
                                  
                                  
                                  
bot.run()
with bot:
         bot.send_message(f"@{SUPPORT}", f"Hello there I'm Online!\nPyroVersion: {pyro}")
