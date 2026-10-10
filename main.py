import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.exceptions import TelegramForbiddenError
from alembic.config import Config
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from alembic import command
from cover_providers.deezer import get_deezer_uri
from cover_providers.itunes import get_itunes_uri
from database.models import async_main
from database.requests import get_cover, set_cover
from handlers import commands
from utils.config import NOW_PLAYING, TOKEN, UPDATE_INTERVAL
from utils.image import load_and_process
from utils.lastfm import (
	get_current_track,
	get_lastfm_cover_uri,
	get_lastfm_uri,
	get_recent_track,
)
from utils.pack import check_pack, update_pack, update_pack_file_id, update_pack_title
from utils.status import set_not_playing_status, set_status

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

last = ''
last_uri = ''

async def _on_startup(scheduler: AsyncIOScheduler):
	await async_main()
	alembic_cfg = Config("alembic.ini")
	await asyncio.to_thread(command.upgrade, alembic_cfg, "head")
	await check_pack(bot)
	try:
		await update()
		scheduler.add_job(update, 'interval', seconds=UPDATE_INTERVAL)
	except TelegramForbiddenError:
		logger.error("Not enough rights to set status. Please, go to the bot, send /start and submit the permission. After that, restart the script")

async def update():
	global last, last_uri, bot
	if NOW_PLAYING is True:
		track = get_current_track()
	else:
		track = get_recent_track()
	if last != track:
		if track is None:
			await set_not_playing_status(bot)
		else:
			await update_pack_title(bot, track)
			file_id = await get_cover(get_lastfm_uri(track))
			try:
				if file_id is not None:
					await update_pack_file_id(bot, file_id)
					await set_status(bot)
				else:
					raise Exception
			except:
				cover_url = get_lastfm_cover_uri(track)
				if cover_url is None:
					cover_url = get_itunes_uri(track)
				if cover_url is None:
					cover_url = get_deezer_uri(track)
				if last_uri != cover_url and cover_url is not None:
					if last_uri != cover_url:
						last_uri = cover_url
						cover = load_and_process(cover_url)
						file_id = await update_pack(bot, cover)
						await set_cover(get_lastfm_uri(track), file_id)
						await set_status(bot)
					else:
						file_id = await get_cover(get_lastfm_uri(last))
						await set_cover(get_lastfm_uri(track), file_id)
				if cover_url is None and NOW_PLAYING is True:
					await set_not_playing_status(bot)
		last = track
 
async def main():
	scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
	scheduler.start()
	dp.include_routers(commands.router)

	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot, on_start=await _on_startup(scheduler), handle_signals=False)

if __name__ == "__main__":
	asyncio.run(main())