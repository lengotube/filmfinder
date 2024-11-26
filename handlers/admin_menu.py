from loader import dp, bot, bot_version
from data.db import get_AllUser, get_AllFilms, get_AllSearch
from aiogram import types
from keybord_s import admin
from myFilters.admin import IsAdminM
from datetime import datetime, timedelta
import aiogram

#вызов admin меню#
@dp.message_handler(IsAdminM(), text=['/admin','Админ меню'])
async def cmd_admin(message: types.Message):
    message_data=await message.answer(f'<b>Загрузка...</b>', reply_markup=admin.admin_menu_main, parse_mode=types.ParseMode.HTML)
    microsecond_too=datetime.now().microsecond
    minute_too=datetime.now().minute
    hour_too=datetime.now().hour
    data_tooday=datetime.now()+timedelta(hours=23-hour_too, minutes=59-minute_too, microseconds=1000000-microsecond_too)
    daynow_too=datetime.now()-timedelta(hours=hour_too, minutes=minute_too, microseconds=microsecond_too)
    user_today=int()
    for i in await get_AllUser(type='user_unix'):
        if i[0] <= data_tooday.timestamp() and i[0] >= daynow_too.timestamp():
            user_today+=1

    all_search_film=await get_AllSearch()
    data_search_film=dict()
    for i in all_search_film:
        data_search_film[i[0]]=i[1]
    try:
        max_rt_film=max(data_search_film)
    except:
        max_rt_film='Нет'
    text_munu=f'<b>📊Статистика📊\n\n👥Всего пользователей: {len(await get_AllUser())}\n🍜Сегодняшние пользователи: {user_today}\n\n➖➖➖➖➖➖➖➖➖\n\n🎬Всего фильмов по коду: {len(await get_AllFilms())}\n🎞Макс по запросом: {max_rt_film}({data_search_film.get(max_rt_film)})</b>'
    await bot.edit_message_text(chat_id=message.from_user.id, message_id=message_data.message_id, text=text_munu, reply_markup=admin.admin_menu_main, parse_mode=types.ParseMode.HTML)
