from loader import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from states import user as ustate
from keybord_s.user import kb_back, get_Favourites_kb
from keybord_s.ohter import ikb_close
from data.db import get_text, get_AllFranchise, get_UserAllFavourites

@dp.message_handler(text='Поиск🔍')
async def search_kb(message: types.Message, state: FSMContext):
    msg=await message.answer('<b>Отправь мне название кино или его код🎫</b>', reply_markup=kb_back, parse_mode=types.ParseMode.HTML)
    await ustate.User_State.search_film.text.set()
    

@dp.message_handler(text='Избранное🌟')
async def favoriite_get_user(message: types.Message):
    await message.answer('Ваш список избранных кино', reply_markup=await get_Favourites_kb(user_id=message.from_user.id))