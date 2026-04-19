from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import os	
import dotenv 

from keyboards.start import kb_start

from utils.lastfm import get_recent_track, get_lastfm_uri
from utils.image import process_buf
from utils.pack import get_file_id
from cover_providers.custom_cover import write_cover

router = Router()

class UserState(StatesGroup):
	waiting_for_emoji = State()
	waiting_for_cover = State()

@router.message(Command("start"))
async def cmd_start(message: Message):
	await message.reply("To give ability for this bot to automatically change your Telegram Premium status, please click on webapp button and grant the permission", reply_markup=kb_start())

@router.message(Command("custom_emoji"))
async def cmd_custom_emoji(message: Message, state: FSMContext):
	await message.answer("Please send the custom emoji you want to use.")
	await state.set_state(UserState.waiting_for_emoji)

@router.message(UserState.waiting_for_emoji)
async def process_emoji(message: Message, state: FSMContext):
	if message.text and message.text.startswith('/'):
		await message.answer("Invalid input. Please send a custom emoji.")
		return
	
	custom_emoji_id = None

	if message.entities:
		for entity in message.entities:
			if entity.type == 'custom_emoji':
				custom_emoji_id = entity.custom_emoji_id
				os.environ['CUSTOM_EMOJI'] = custom_emoji_id
				
				dotenv_file = dotenv.find_dotenv()
				dotenv.load_dotenv(dotenv_file)
				
				dotenv.set_key(dotenv_file, 'CUSTOM_EMOJI', os.environ['CUSTOM_EMOJI'])
				break

	if custom_emoji_id:
		await message.answer(f"Custom emoji set successfully!")
		await state.clear()
		
@router.message(Command("custom_cover"))
async def cmd_custom_cover(message: Message, state: FSMContext):
	track = get_recent_track()
	await state.update_data(track=get_lastfm_uri(track))
	await message.answer(f"Please send cover for {track} you want to use")
	await state.set_state(UserState.waiting_for_cover)

@router.message(UserState.waiting_for_cover)
async def process_emoji(message: Message, state: FSMContext):
	data = await state.get_data()
	
	if message.photo:
		input_file = await message.bot.download(message.photo[-1])
		cover = process_buf(input_file)
		file_id = await get_file_id(message, cover)
		await write_cover(data['track'], file_id)
		await message.answer(f"Custom cover set successfully!")
		await state.clear()