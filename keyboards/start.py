from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def kb_start():
    inline_kb_list = [
        [InlineKeyboardButton(text="Grant the permission", web_app=WebAppInfo(url='https://ugliestie.github.io/emojistatuspermission/'))]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)