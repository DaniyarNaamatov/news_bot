from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config


TOKEN = config("TOKEN")
bot = Bot(TOKEN)