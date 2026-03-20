from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.start import kb_start

from utils.lastfm import get_recent_track, get_lastfm_uri
from utils.itunes import get_itunes_uri
from utils.image import load_and_process
from utils.pack import update_pack
from utils.status import set_status

import time
from main import logger

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
	await message.reply("To give ability for this bot to automatically change your Telegram Premium status, please click on webapp button and grant the permission", reply_markup=kb_start())

@router.message(Command("update"))
async def cmd_start(message: Message):
	await message.reply("Start!")
	last = None
	while True:
			"""await check_pack(message)"""
			track = get_recent_track()
			if last != track:
				uri = get_lastfm_uri(track)
				logger.warning(uri)
				if uri is None:
					uri = get_itunes_uri(track)
				if uri is not None:
					cover = load_and_process(uri)
					await update_pack(message, cover)
					await set_status(message)
				last = track
			time.sleep(10)