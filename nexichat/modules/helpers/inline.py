from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from nexichat import OWNER
from nexichat import nexichat

DEV_OP = [
    [
        InlineKeyboardButton(text="🌸ᴏᴡɴᴇʀ🌸", user_id=OWNER),
        InlineKeyboardButton(text="💐ᴜᴘᴅᴀᴛᴇs💐", url=f"https://t.me/new_heroku_cc"),
    ],
    [
        InlineKeyboardButton(
            text="🔺𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ🔺",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
       # InlineKeyboardButton(text="🤨𝗦ᴏᴜʀᴄᴇ😑", callback_data="SOURCE"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="😍 𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ 😍",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="𝗖𝗹𝗼𝘀𝗲",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="𝗕𝗮𝗰𝗸", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="🤖𝗖ʜᴀᴛ𝐁ᴏᴛ🤖", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="👻𝗧ᴏᴏʟs👻", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="𝗕𝗮𝗰𝗸", callback_data="BACK"),
        InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [ᴘ
    [
        InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="𝗘𝗻𝗮𝗯𝗹𝗲", callback_data=f"addchat"),
        InlineKeyboardButton(text="𝗗𝗶𝘀𝗮𝗯𝗹𝗲", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="𝗦𝗼𝗼𝗻", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="𝗕𝗮𝗰𝗸", callback_data="SBACK"),
        InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="𝗕𝗮𝗰𝗸", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="« 𝗛𝗲𝗹𝗽 »", callback_data="HELP"),
        InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="« ʜᴇʟᴘ »", url=f"https://t.me/{nexichat.username}?start=help"
        ),
        InlineKeyboardButton(text="", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="« 𝗛𝗲𝗹𝗽 »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="😎𝗢ᴡɴᴇʀ", user_id=OWNER),
     #   InlineKeyboardButton(text="⚠️𝗦ᴏᴜʀᴄᴇ⚠️", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="🍁𝗨ᴘᴅᴀᴛᴇs🍁", url=f"https://t.me/new_heroku_cc"),
        InlineKeyboardButton(text="𝗕𝗮𝗰𝗸", callback_data="BACK"),
    ],
]
