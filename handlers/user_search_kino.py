from loader import bot, dp, rate_searsh
from aiogram import types
from aiogram.dispatcher import FSMContext
from keybord_s.user import kb_films, sub_list, kb_user
from misc.chek_chennel import check as sub_check
from data.db import add_historyInSearch
from data.db import only_list, get_AllFilms, get_dataUser, get_text, get_films, add_filmname, get_filmname
from states import user as ustate
from misc.search_film import search
from misc.plugin.KinoPoiskFree import get_FilmsMe
from myFilters.user import IsCode

async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer(f'Фильм можно найти раз в {rate_searsh} секунд😪', reply_markup=await kb_user(m.from_user.id))
    state = dp.current_state(chat=m.from_user.id, user=m.from_user.id)
    await state.set_state(None)

async def spisok_number_to60():
    counter_number=int()
    list_rt=str()
    while counter_number != 60:
        counter_number+=1
        list_rt+=f'{str(counter_number)} '
    list_rt=list_rt.split()
    return list_rt

@dp.message_handler(state=ustate.User_State.search_film.text)
@dp.throttled(anti_flood, rate=rate_searsh)
async def search_kino_parser(message: types.Message, state: FSMContext):
    await state.finish()
    if message.text == 'Отмена❌':
        await message.answer('Отмена❌', reply_markup=await kb_user(message.from_user.id))
        return
    async def check(message: types.Message):
        data_code=await only_list(await get_AllFilms(type='films_code'))
        for i in data_code:
            if i == message.text:
                return True
        return False
    if await sub_check(user_id=message.from_user.id):
            await bot.send_message(chat_id=message.from_user.id, text='Вы не подписаны на канал(ы)❌\nПосле подписки повторите попытку👌', reply_markup=await sub_list())
            return
    if await check(message):
        if await sub_check(user_id=message.from_user.id):
            await bot.send_message(chat_id=message.from_user.id, text='Вы не подписаны на канал(ы)❌\nПосле подписки повторите попытку👌', reply_markup=await sub_list())
            return

        await message.answer(f'Фильм найден!', reply_markup=await kb_user(message.from_user.id))
        film_data=await get_films(code=message.text)
        text_film=await get_text(type='text_text', text_type='film')
        text_film=text_film[0][0]
        me=await bot.get_me()
        text_film=str(text_film).replace('{username_bot}', me.mention)
        text_film=str(text_film).replace('{bot_id}', str(me.id))
        text_film=str(text_film).replace('{username}', message.from_user.mention)
        text_film=str(text_film).replace('{full_name}', message.from_user.full_name)
        text_film=str(text_film).replace('{user_id}', str(message.from_user.id)) 
        text_film=str(text_film).replace('{film_name}', film_data[0][1]) 
        
        data_film=await search(name_film=film_data[0][1])
        ikb_films=await kb_films(name_films=film_data[0][3], user_id=message.from_user.id, type=data_film.type_kino_, id=data_film.id_)
        await bot.send_photo(chat_id=message.from_user.id, photo=film_data[0][2], caption=text_film, reply_markup=ikb_films, parse_mode=types.ParseMode.HTML)
    else:
        try:
            data_film=await search(name_film=message.text)
            id = await add_filmname(message.text)
            await bot.send_photo(chat_id=message.from_user.id, photo=data_film.photo_, caption=f'<b>🎥 {data_film.type_kino_}:</b> <code>{data_film.name_film_}</code>\n\n🗓 Год производства: {data_film.year_}\n\n<b>👁 Жанры: {data_film.genre_}\n\n👥{data_film.text_autor_}: {data_film.director_}\n\n🔗 Длительность: {data_film.length_} мин</b>', reply_markup=await kb_films(name_films=id, user_id=message.from_user.id, type=data_film.type_kino_, id=data_film.id_), parse_mode=types.ParseMode.HTML)
            await add_historyInSearch(name=data_film.name_film_)
            await message.answer(f'Следующий запрос можно будет сделать через {rate_searsh}😴', reply_markup=await kb_user(message.from_user.id))
        except Exception as ex:
            print(ex)
            await message.answer('Нам не удолось найти фильм😥')
            await message.answer(f'Следующий запрос можно будет сделать через {rate_searsh}😴', reply_markup=await kb_user(message.from_user.id))