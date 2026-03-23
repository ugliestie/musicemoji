from aiogram import Bot

from utils.config import USER_ID, BOT_USERNAME, CUSTOM_EMOJI

async def set_status(bot: Bot):
    set = await bot.get_sticker_set(name = f'p_{USER_ID}_by_{BOT_USERNAME}')
    id = set.stickers[0].custom_emoji_id
    await bot.set_user_emoji_status(
        user_id=USER_ID,
        emoji_status_custom_emoji_id=id
    )
    
async def set_not_playing_status(bot: Bot):
    await bot.set_user_emoji_status(
        user_id=USER_ID,
        emoji_status_custom_emoji_id=CUSTOM_EMOJI
    )