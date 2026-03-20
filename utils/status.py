from aiogram.types import Message

from utils.config import USER_ID, BOT_USERNAME

async def set_status(message: Message):
    set = await message.bot.get_sticker_set(name = f'p_{USER_ID}_by_{BOT_USERNAME}')
    id = set.stickers[0].custom_emoji_id
    await message.bot.set_user_emoji_status(
        user_id=USER_ID,
        emoji_status_custom_emoji_id=id
    )