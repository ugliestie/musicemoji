from aiogram.types import StickerSet, InputSticker, Message
from aiogram.types import FSInputFile, BufferedInputFile
from aiogram.exceptions import TelegramBadRequest
import io

from main import logger

from utils.config import USER_ID, BOT_USERNAME

'''async def check_pack(message: Message):
    await message.bot.create_new_sticker_set(
            user_id=USER_ID,
            name=f'p_{USER_ID}_by_{BOT_USERNAME}',
            title='github.com/ugliestie/musicemoji',
            stickers=[InputSticker(
                sticker=FSInputFile("blank.png"),
                format='static',
                emoji_list=['🎵'])],
            sticker_type='custom_emoji')'''

async def update_pack(message: Message, cover: bytes):
    set = await message.bot.get_sticker_set(name = f'p_{USER_ID}_by_{BOT_USERNAME}')
    old_emoji = set.stickers[0].file_id
    sticker = InputSticker(
                sticker=BufferedInputFile(cover, "cover.png"),
                format='static',
                emoji_list=['🎵'])
    await message.bot.replace_sticker_in_set(
        user_id=USER_ID,
        name=f'p_{USER_ID}_by_{BOT_USERNAME}',
        old_sticker=old_emoji,
        sticker=sticker
    )
    
