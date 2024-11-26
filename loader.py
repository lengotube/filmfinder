from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import *

#Connect к боту#
storage=MemoryStorage()
bot=Bot(token)
dp=Dispatcher(bot, storage=storage)
bot_version='1.9'
