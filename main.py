import asyncio
import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram import BaseMiddleware

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from utils.config import TOKEN

from utils.lastfm import get_recent_track, get_lastfm_uri
from utils.itunes import get_itunes_uri
from utils.image import load_and_process
from utils.pack import check_pack, update_pack
from utils.status import set_status

from keyboards.start import kb_start

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

router = Router()

last = None

# позволяет доставать scheduler из агрументов фунции
class SchedulerMiddleware(BaseMiddleware):
	def __init__(self, scheduler: AsyncIOScheduler):
		super().__init__()
		self._scheduler = scheduler

	async def __call__(self, handler, event, data):
		# прокидываем в словарь состояния scheduler
		data["scheduler"] = self._scheduler
		return await handler(event, data)

@router.message(Command("start"))
async def cmd_start(message: Message):
	await message.reply("To give ability for this bot to automatically change your Telegram Premium status, please click on webapp button and grant the permission", reply_markup=kb_start())
 
@router.message(Command("update"))
async def hello(message: Message, scheduler: AsyncIOScheduler):
	await message.reply(
		text="Automatic update started working!"
	)
	await check_pack(bot)
	scheduler.add_job(update, 'interval', seconds=15)

async def update():
	global last, bot
	track = get_recent_track()
	if last != track:
		uri = get_lastfm_uri(track)
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
	# регистрируем middleware c scheduler
	dp.update.middleware(
		SchedulerMiddleware(scheduler=scheduler),
	)
	dp.include_routers(router)

	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot, handle_signals=False)

if __name__ == "__main__":
	asyncio.run(main())