import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramForbiddenError

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from utils.config import TOKEN, UPDATE_INTERVAL, NOW_PLAYING

from utils.lastfm import get_recent_track, get_current_track, get_lastfm_uri
from utils.image import load_and_process
from utils.pack import check_pack, update_pack
from utils.status import set_status, set_not_playing_status

from cover_providers.itunes import get_itunes_uri
from cover_providers.deezer import get_deezer_uri

from handlers import commands

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

last = ''

async def _on_startup(scheduler: AsyncIOScheduler):
	await check_pack(bot)
	try:
		await set_status(bot)
		scheduler.add_job(update, 'interval', seconds=UPDATE_INTERVAL)
	except TelegramForbiddenError:
		logger.error("Not enough rights to set status. Please, go to the bot, send /start and submit the permission. After that, restart the script")

async def update():
	global last, bot
	if NOW_PLAYING is True:
		track = get_current_track()
	else:
		track = get_recent_track()
	if last != track:
		if track is None:
			await set_not_playing_status(bot)
		else:
			uri = get_lastfm_uri(track)
			if uri is None:
				uri = get_deezer_uri(track)
			if uri is None:
				uri = get_itunes_uri(track)
			if uri is not None:
				cover = load_and_process(uri)
				await update_pack(bot, cover)
				await set_status(bot)
		last = track
 
async def main():
	scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
	scheduler.start()
	dp.include_routers(commands.router)

	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot, on_start=await _on_startup(scheduler), handle_signals=False)

if __name__ == "__main__":
	asyncio.run(main())