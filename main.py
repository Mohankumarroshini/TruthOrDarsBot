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
**ʜᴇʏ~ {}
 ɪ'ᴍ ᴀ ᴛʀᴜᴛʜᴏʀᴅᴀʀᴇ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ~
 ʙᴇʟᴏᴡ ᴄʜᴇᴄᴋ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs! × ×**
"""

@bot.on_message(filters.command(["start","help"]))
async def start(_, m):
       url = "https://telegra.ph/file/ce4fa9c519495a18ac6ab.jpg"
       await m.reply_photo(photo=url,caption=PM_START_TEXT.format(m.from_user.first_name),
             reply_markup=InlineKeyboardMarkup(buttons))

ABOUT_TEXT = """
**ʜᴇʟʟᴏ ᴅᴇᴀʀ ᴜsᴇʀs!**
`ɪ'ᴍ ᴀ ᴛʀᴜᴛʜᴏʀᴅᴀʀᴇ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ`
`ʜᴀᴠɪɴɢ ᴍᴜʟᴛɪ ʟᴀɴɢᴜᴀɢᴇ`
`ᴜsɪɴɢ ᴀᴘɪ sʏsᴛᴇᴍ`

ᴍʏ ᴘʏʀᴏᴠᴇʀsɪᴏɴ: {}
ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ: [ᴛᴀᴍɪʟʙᴏᴛs](https://t.me/tamilbots)
sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ: [ᴛᴀᴍɪʟsᴜᴘᴘᴏʀᴛ](https://t.me/tamilsupport)

ᴀʟʟ ᴍʏ ᴄʀᴇᴅɪᴛs ɢᴏsᴛᴏ:
[ᴍsᴅ](https://t.me/my_dear_lightbright) 🤗
"""

@bot.on_callback_query(filters.regex("about_back"))
async def about(_, query: CallbackQuery):
           query = query.message
           await query.edit_caption(ABOUT_TEXT.format(pyro),
             reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help_back")]]))
    
LANG_CODE = [[InlineKeyboardButton("ʟᴀɴɢ ᴄᴏᴅᴇ!", callback_data="help_back")]]
    
IMAGE = "https://telegra.ph/file/5a24612aa552df19d65c4.jpg"

TRUTH_STRING = """ ~~ ** ʜᴇʏ! {} ~~**
{} ɢɪʙᴇ ʏᴏᴜ ᴀ ᴛʀᴜᴛʜ! ~ 😳
~~**ʜᴇʀᴇ ᴛʜᴇ ᴛʀᴜᴛʜ**~~: **{}** 😈
~~ **ɴᴏᴡ ᴛᴇʟʟ ᴛʜᴇ ᴛʀᴜᴛʜ ᴛᴏ** ~~: **{}**! 😰
"""

CODES = """ **ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛʀᴜᴛʜ ᴏʀ ᴅᴀʀᴇ ᴛʀᴀɴsʟᴀᴛɪᴏɴ ᴄᴏᴅᴇs!**\n
**ᴇɴɢʟɪsʜ**: `en`
**ʙᴇɴɢᴀʟɪ**: `bn`
**ɢᴇʀᴍᴀᴍ**: `de`
**sᴘᴀɴɪsʜ**: `es`
**ғʀᴇɴᴄʜ**: `fr`
**ʜɪɴᴅɪ**: `hi`
**ᴛᴀɢᴀʟᴏɢ**: `tl`
**ᴛᴀᴍɪʟ**: `ta`

Example: 
- /truth ta: ʀᴇᴘʟʏ ᴛᴏ sᴏᴍᴇᴏɴᴇ!
- /dare ta: ʀᴇᴘʟʏ ᴛᴏ sᴏᴍᴇᴏɴᴇ!

[𝐬𝐮𝐩𝐩𝐨𝐫𝐭](t.me/tamilSupport) | [𝐮𝐩𝐝𝐚𝐭𝐞𝐬](t.me/tamilbots)
"""
ta_truth = ("நீங்கள் யாரையாவது பேசுபவரா? "
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
    "நீங்கள் எப்போதாவது யாரையாவது சோதனை செய்து பிடிபட்டீர்களா?")
         
@bot.on_message(filters.command("truth"))
async def truth(_, m):
       reply = m.reply_to_message
       API = requests.get("https://api.truthordarebot.xyz/v1/truth").json()
       English = API["question"]
       Bengali = API["translations"]["bn"]
       German = API["translations"]["de"]
       Spanish = API["translations"]["es"]
       French = API["translations"]["fr"]
       Hindi = API["translations"]["hi"]
       Tagalog = API["translations"]["tl"]
       Tamil = random.choice(ta_truth)
       if len(m.command) < 2:
             await m.reply_photo(IMAGE,caption="ʙᴀᴋᴀ! ʀᴇᴀᴅ ᴛʜᴇ ʟᴀɴɢ ᴄᴏᴅᴇ!😑",
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
               return 
           if text.endswith("ta"):
               await reply.reply_photo(IMAGE,caption=TRUTH_STRING.format(name1,name2,Tamil,name2))
               return 
           if text.endswith("en"):
               await reply.reply_photo(IMAGE,caption=TRUTH_STRING.format(name1,name2,English,name2))
          
        

ta_dare = (
    "உங்கள் தொலைபேசியில் மிகவும் சங்கடமான புகைப்படத்தைக் காட்டு "
    "நீங்கள் குறுஞ்செய்தி அனுப்பிய கடைசி ஐந்து நபர்களையும் செய்திகள் என்ன சொல்கின்றன என்பதையும் காட்டுங்கள்",
    "உங்கள் இன்ஸ்டாகிராம் கணக்கிலிருந்து மற்ற குழுவை டிஎம் செய்ய விடுங்கள்",
    "ஒரு பச்சைப் பூண்டு சாப்பிடுங்கள்",
    "100 குந்துகைகள் செய்யுங்கள்",
    "ூன்று ஐஸ் கட்டிகள் உருகும் வரை உங்கள் வாயில் வைத்திருங்கள்",
    "உங்கள் இடதுபுறத்தில் உள்ள நபரிடம் ஏதாவது அழுக்காகச் சொல்லுங்கள் உங்களுக்கு நிறுவனம் கிடைத்துள்ளது!",
    "உங்கள் வலது பக்கத்தில் இருப்பவருக்கு கால் மசாஜ் செய்யுங்கள்",
    "கிடைக்கக்கூடிய 10 வெவ்வேறு திரவங்களை ஒரு கோப்பையில் போட்டு குடிக்கவும்",
    "*உங்கள் மனதில் வரும் முதல் வார்த்தையை கத்துங்கள்",
    "உங்களுக்கு விருப்பமான ஒருவருக்கு மடியில் நடனம் கொடுங்கள்",
    "நான்கு ஆடைகளை அகற்று"
    "உங்கள் பேஸ்புக் நியூஸ்ஃபீடில் முதல் 15 இடுகைகளைப் போல",
    "ஒரு ஸ்பூன்ஃபுல் கடுகு சாப்பிடுங்கள்",
    "நீங்கள் மீண்டும் செல்லும் வரை கண்களை மூடிக்கொண்டு இருங்கள்",
    "உங்கள் தொலைபேசி புத்தகத்தில் கடைசி நபருக்கு ஆறாவது அனுப்புங்கள்",
    "உங்கள் உச்சகட்ட முகத்தைக் காட்டுங்கள்",
    "ஒரு வாழைப்பழத்தை கவர்ச்சியாக சாப்பிடு"
    "உங்கள் பணப்பயை காலி செய்து உள்ளே இருப்பதை அனைவருக்கும் காட்டுங்கள்",
    "உங்கள் சிறந்த கவர்ச்சியான வலைவலையைச் செய்யுங்கள்",
    "உங்கள் வலதுபுறத்தில் 10 நிமிடங்களுக்கு ஒரு நபராக பாசாங்கு செய்யுங்கள்",
    "உங்கள் கைகளைப் பயன்படுத்தாமல் ஒரு சிற்றுண்டியை சாப்பிடுங்கள்",
    "குழுவில் உள்ள அனைவரையும் பற்றி இரண்டு நேர்மையான விஷயங்களைச் சொல்லுங்கள்",
    "ஒரு நிமிடம் இருங்கள்",
    "குழுவை சீக்கிரம் சிரிக்க வைக்க முயற்சி செய்யுங்கள்",
    "உங்கள் முழு முஷ்டியையும் உங்கள் வாயில் வைக்க முயற்சி செய்யுங்கள்",
    "உங்களைப் பற்றி ஒரு சங்கடமான கதையை அனைவருக்கும் சொல்லுங்கள்",
    "உங்கள் முழங்கையை நக்க முயற்சி செய்யுங்கள்",
    "இன்ஸ்டாகிராம் கதைகளில் உங்கள் தொலைபேசியில் பழமையான செல்ஃபியை இடுகையிடவும்",
    "உங்களுக்குத் தெரிந்த சோகமான கதையைச் சொல்லுங்கள்",
    "ஓநாய் போல இரண்டு நிமிடங்கள் அலறுங்கள்",
    "இரண்டு நிமிடங்கள் இசை இல்லாமல் நடனமாடுங்கள்",
    "ஒரு கற்பனை துருவத்துடன் துருவ நடனம்",
    "வேறொருவர் உங்களை கூச்சப்படுத்தி சிரிக்காமல் இருக்க முயற்சி செய்யுங்கள்",
    "உங்களால் முடிந்தவரை ஒரே நேரத்தில் பல சிற்றுண்டிகளை உங்கள் வாயில் போடுங்கள்",
    "உங்கள் சமீபத்திய செல்ஃபி அனுப்பவும்."
    "உங்கள் அசிங்கமான செல்ஃபி அனுப்பவும்."
    "உங்கள் முகநூல் தேடல் வரலாற்றின் ஸ்கிரீன் ஷாட்டை அனுப்பவும்",
    "உங்கள் கேலரியின் ஸ்கிரீன் ஷாட்டை அனுப்பவும்."
    "உங்கள் மெசஞ்சர் இன்பாக்ஸின் ஸ்கிரீன் ஷாட்டை அனுப்பவும்",
    "மிகவும் நெருக்கமாக ஏதாவது சொல்லுங்கள்.",
    "உங்கள் ட்விட்டர் இன்பாக்ஸின் ஸ்கிரீன் ஷாட்டை அனுப்பவும்",
    "உங்கள் முகப்புத் திரையின் ஸ்கிரீன் ஷாட்டை அனுப்பவும்.",
    "உங்களுக்குப் பிடித்த பாடலின் அட்டையை அனுப்பவும். 🎤",
    "யாராவது ஒரு பாடல் நகைச்சுவை செய்து ஆதாரத்தை அனுப்புங்கள்.",
    "உங்கள் தற்போதைய ஈர்ப்பை ஒப்புக்கொள்ளுங்கள். ❤️",
    "உங்கள் உண்மையான அன்பு யார் என்பதை அறிவிக்கவும்."
    "உங்கள் கேலரியின் ஸ்கிரீன் ஷாட்டை அனுப்பவும்."
    "நீங்கள் உங்கள் பக்கத்து வீட்டு மகளை நேசித்தீர்களா?"
    "உங்கள் கிரஷின் படத்தை உங்கள் டிபியாக அமைக்கவும்.",
    "எனக்கு அதிக தைரியத்தை பரிந்துரைக்கவும்.")

DARE_STRING = """ ~~ ** ʜᴇʏ! {} ~~**
{} ɢᴀᴠᴇ ʏᴏᴜ ᴀ ᴅᴀʀᴇ! ~ 😳
~~**ʜᴇʀᴇ ɪs ᴛʜᴇ ᴛʀᴜᴛʜ**~~: **{}** 😈
~~ **ɴᴏᴡ ᴅᴏ ᴛʜᴇ ᴅᴀʀᴇ!** ~~ **{}**! 😰
"""

@bot.on_message(filters.command("dare"))            
async def dare(_, m):
       reply = m.reply_to_message
       API = requests.get("https://api.truthordarebot.xyz/v1/dare").json()
       English = API["question"]
       Bengali = API["translations"]["bn"]
       German = API["translations"]["de"]
       Spanish = API["translations"]["es"]
       French = API["translations"]["fr"]
       Hindi = API["translations"]["hi"]
       Tagalog = API["translations"]["tl"]
       Tamil = random.choice(ta_dare)
       if len(m.command) < 2:
           await m.reply_photo(IMAGE,caption="ʙᴀᴋᴀ! ʀᴇᴀᴅ ᴛʜᴇ ʟᴀɴɢs ᴄᴏᴅᴇ!😑",
           reply_markup=InlineKeyboardMarkup(LANG_CODE))
           return
       text = m.text.split(None, 1)[1]
       name1 = reply.from_user.first_name
       name2 = m.from_user.first_name
       if reply:
           if text.endswith("bn"):
               await reply.reply_photo(IMAGE,caption=DARE_STRING.format(name1,name2,Bengali,name2))
               return
           if text.endswith("de"):
               await reply.reply_photo(IMAGE,caption=DARE_STRING.format(name1,name2,German,name2))
               return
           if text.endswith("es"):
               await reply.reply_photo(IMAGE,caption=DARE_STRING.format(name1,name2,Spanish,name2))
               return
           if text.endswith("fr"):
               await reply.reply_photo(IMAGE,caption=DARE_STRING.format(name1,name2,French,name2))
               return
           if text.endswith("hi"):
               await reply.reply_photo(IMAGE,caption=DARE_STRING.format(name1,name2,Hindi,name2))
               return
           if text.endswith("tl"):
               await reply.reply_photo(IMAGE,caption=DARE_STRING.format(name1,name2,Tagalog,name2))
               return 
           if text.endswith("ta"):
               await reply.reply_photo(IMAGE,caption=DARE_STRING.format(name1,name2,Tamil,name2))
               return
           if text.endswith("en"):
               await reply.reply_photo(IMAGE,caption=TRUTH_STRING.format(name1,name2,English,name2))
          
 
CLOSE = [[InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close"),
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about_back")]]
    
@bot.on_callback_query(filters.regex("help_back"))
async def helpback(_, query: CallbackQuery):
        await query.message.edit_caption(CODES,
        reply_markup=InlineKeyboardMarkup(CLOSE))
        
@bot.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
        await query.message.delete()

                                  
                                  
                                  
bot.run()
with bot:
         bot.send_message(f"@{SUPPORT}", f"Hello there I'm Online!\nPyroVersion: {pyro}")
