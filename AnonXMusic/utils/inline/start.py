from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
                [ 
             InlineKeyboardButton( 
                 text="𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽", 
                 url=f"https://t.me/{BOT_USERNAME}?startgroup=true", 
             ) 
         ], 
         [ 
             InlineKeyboardButton( 
                 text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="settings_back_helper" 
             ) 
         ], 
         [ 
             InlineKeyboardButton( 
                 text=" ❰𝗖𝗵𝗮𝗻𝗻𝗲𝗹❱", url=config.SUPPORT_CHANNEL 
             ), 
             InlineKeyboardButton( 
                 text=" ❰𝗚𝗿𝗼𝘂𝗽❱ ", url=config.SUPPORT_GROUP 
             ) 
         ], 
         [ 
InlineKeyboardButton( 
                 text=" ❰𝙍𝙚𝙥𝙤❱", callback_data="lipps_xd" 
             ), 
             InlineKeyboardButton( 
                 text=" ❰𝙊𝙬𝙣𝙚𝙧❱", url="https://t.me/ITS_HELLL_BOYYY" 
             ) 
         ] 
      ]
    return buttons
