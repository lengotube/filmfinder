from loader import dp, bot, admin_id
from aiogram import types
from myFilters.user import IsCode
from data.db import get_films, get_error_link_complaint_unix, update_error_link_complaint_unix, get_text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from time import time
from misc.chek_chennel import check as sub_check
from keybord_s.ohter import ikb_close
from keybord_s.user import kb_films, sub_list
from datetime import datetime, timedelta

#Обработка кнопки "Одна из сыллок не работает❓"#
@dp.callback_query_handler(text='link_no_work')
async def Link_complaint(call: types.CallbackQuery):
    if await get_error_link_complaint_unix(user_id=call.from_user.id) == None or await get_error_link_complaint_unix(user_id=call.from_user.id) <= time():
        await call.message.answer('Мы отправили администратуру ошибку☑️', reply_markup=ikb_close)
        await bot.send_message(chat_id=admin_id[0], text=f'Пользователь <a href="tg://user?id={call.from_user.id}">{call.from_user.full_name}</a> пожаловался то что одна из сыллок не работает❗️', parse_mode=types.ParseMode.HTML, reply_markup=ikb_close.row(InlineKeyboardButton(text='Проверить каналы⚛️', callback_data='check_chennel_admin')))
        timeub=datetime.now()+timedelta(hours=3)
        await update_error_link_complaint_unix(user_id=call.from_user.id, time_ub=timeub.timestamp())
    else:
        await call.answer('Вы уже жаловались❌')