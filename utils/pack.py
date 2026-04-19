from aiogram import Bot
from aiogram.types import Message
from aiogram.types import InputSticker
from aiogram.types import FSInputFile, BufferedInputFile

from utils.config import USER_ID, BOT_USERNAME

async def check_pack(bot: Bot):
	try:
		await bot.get_sticker_set(name = f'p_{USER_ID}_by_{BOT_USERNAME}')
	except:
		await bot.create_new_sticker_set(
			user_id=USER_ID,
			name=f'p_{USER_ID}_by_{BOT_USERNAME}',
			title='github.com/ugliestie/musicemoji',
			stickers=[InputSticker(
				sticker=FSInputFile("blank.png"),
				format='static',
				emoji_list=['🎵'])],
			sticker_type='custom_emoji')

async def update_pack(bot: Bot, cover: bytes):
	set = await bot.get_sticker_set(name = f'p_{USER_ID}_by_{BOT_USERNAME}')
	old_emoji = set.stickers[0].file_id
	sticker = InputSticker(
				sticker=BufferedInputFile(cover, "cover.png"),
				format='static',
				emoji_list=['🎵'])
	await bot.replace_sticker_in_set(
		user_id=USER_ID,
		name=f'p_{USER_ID}_by_{BOT_USERNAME}',
		old_sticker=old_emoji,
		sticker=sticker
	)
 
async def update_pack_file_id(bot: Bot, file_id: str):
	set = await bot.get_sticker_set(name = f'p_{USER_ID}_by_{BOT_USERNAME}')
	old_emoji = set.stickers[0].file_id
	sticker = InputSticker(
				sticker=file_id,
				format='static',
				emoji_list=['🎵'])
	await bot.replace_sticker_in_set(
		user_id=USER_ID,
		name=f'p_{USER_ID}_by_{BOT_USERNAME}',
		old_sticker=old_emoji,
		sticker=sticker
	)

async def get_file_id(message: Message, cover: bytes):
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
		set = await message.bot.get_sticker_set(name = f'p_{USER_ID}_by_{BOT_USERNAME}')
		return set.stickers[0].file_id
