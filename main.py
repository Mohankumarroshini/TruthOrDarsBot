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
    
LANG_CODE = [[InlineKeyboardButton("Lang Codes!", callback_data="lang_codes")]]
    
IMAGE = "http://telegra.ph/file/c50b1959b61acf73f0a57.jpg"

TRUTH_STRING = """ ~~ ** Hey! {} ~~**
{} give you a Truth! ~ 😳
~~**Here the truth**~~: **{}** 😈
~~ **Now tell the truth to** ~~: **{}**! 😰
"""

CODES = """ **The list of available truth or dare translation codes!**\n
**Bengali**: `bn`
**German**: `de`
**Spanish**: `es`
**French**: `fr`
**Hindi**: `hi`
**Tagalog**: `tl`
"""
ta = ("நீங்கள் யாரையாவது பேசுபவரா? "
     "உங்கள் பெற்றோர்கள் 'அதை' செய்வதை நீங்கள் எப்போதாவது நடந்திருக்கிறீர்களா?",
    "உங்களுக்கு மிகவும் பிடித்த கடைசி நபர் யார்? ஏன்?"
    "நீங்கள் எப்போதாவது பள்ளியில் இருந்து இடைநீக்கம் செய்யப்பட்டிருக்கிறீர்களா?"
    "நிர்வாணமாக செல்வதற்கோ அல்லது உங்கள் எண்ணங்கள் உங்கள் தலைக்கு மேலே உள்ள சிந்தனை குமிழிகளில் தோன்றுவதற்கோ இடையில் நீங்கள் படிக்க வேண்டியிருந்தால், நீங்கள் எதை தேர்வு செய்வீர்கள்?",
    "நீங்கள் இழக்க பயப்படும் ஒரு விஷயம் என்ன?",
    "இந்த நேரத்தில் நீங்கள் யாரையாவது விரும்புகிறீர்களா?",
    "உங்கள் சிறந்த நண்பரைப் பற்றி நீங்கள் பொறாமைப்படுகிறீர்களா?",
    "ஒரு பணக்காரனுக்காக உங்கள் காதலனை ஏமாற்றுவீர்களா?"
    "உங்கள் மிகப்பெரிய திருப்பம் என்ன?",
    "உங்கள் பெற்றோரிடம் கடைசியாக எப்போது பொய் சொன்னீர்கள், ஏன்?"
    "உங்கள் சிறந்த கூட்டாளரை விவரிக்கவும்."
    "நீங்கள் செய்த பயங்கரமான விஷயம் என்ன?",
    "நீங்கள் எப்போதாவது உங்கள் மூக்கை எடுத்து சாப்பிட்டீர்களா?",
    "உங்கள் பெற்றோரிடம் கடைசியாக எப்போது பொய் சொன்னீர்கள், ஏன்?"
    "நீங்கள் எப்போதாவது ஒரு காதலியை ஆன்லைனில் பதிவு செய்ய முயற்சித்தீர்களா?",
    "ஒரு பெண்ணை வாடகைக்குப் பார்த்த பிறகு, உங்களுக்கும் ஆன்லைனில் ஜிஎஃப் புக்கிங்கில் ஆர்வம் இருக்கிறதா?",
    "போட்டியில் பங்கேற்க உங்கள் வயது குறித்து நீங்கள் எப்போதாவது பொய் சொல்லியிருக்கிறீர்களா?" ,
    "நீங்கள் எப்போதாவது யாரையாவது சோதனை செய்து பிடிபட்டீர்களா?" ]
         
@bot.on_message(filters.command("truth"))
async def truth(_, m):
       reply = m.reply_to_message
       API = requests.get("https://api.truthordarebot.xyz/v1/truth").json()
       Bengali = API["translations"]["bn"]
       German = API["translations"]["de"]
       Spanish = API["translations"]["es"]
       French = API["translations"]["fr"]
       Hindi = API["translations"]["hi"]
       Tagalog = API["translations"]["tl"]
       if len(m.command) < 2:
             await m.reply_photo(IMAGE,caption="baka! read the langs codes!😑",
             reply_markup=InlineKeyboardMarkup(LANG_CODE))
             return
       text = m.text.split(None, 1)[1]
       name1 = reply.from_user.first_name
       name2 = m.from_user.first_name
       if reply:
           if text.endswith("bn"):
               await reply.reply_photo(IMAGE,caption=TRUTH_STRING.format(name1,name2,Bengali,name2))
               return
           if text.endswith("de"):
               await reply.reply_photo(IMAGE,caption=TRUTH_STRING.format(name1,name2,German,name2))
               return
           if text.endswith("es"):
               await reply.reply_photo(IMAGE,caption=TRUTH_STRING.format(name1,name2,Spanish,name2))
               return
           if text.endswith("fr"):
               await reply.reply_photo(IMAGE,caption=TRUTH_STRING.format(name1,name2,French,name2))
               return
           if text.endswith("hi"):
               await reply.reply_photo(IMAGE,caption=TRUTH_STRING.format(name1,name2,Hindi,name2))
               return
           if text.endswith("tl"):
               await reply.reply_photo(IMAGE,caption=TRUTH_STRING.format(name1,name2,Tagalog,name2))
               

                                  
@bot.on_callback_query(filters.regex("lang_codes"))
async def langs(_, query: CallbackQuery):
        await query.message.edit_caption(CODES)
                                  
                                  
                                  
                                  
bot.run()
with bot:
         bot.send_message(f"@{SUPPORT}", f"Hello there I'm Online!\nPyroVersion: {pyro}")
