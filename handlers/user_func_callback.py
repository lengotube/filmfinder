from loader import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from data.db import add_favourite, delete_favourite, add_filmname, get_filmname
from myFilters.user import IsinFavourites, IsDeleteFavourites, IsSearchWCall
from keybord_s.user import kb_films, get_Favourites_kb
from misc.search_film import search

@dp.callback_query_handler(IsSearchWCall())
async def search_fim_with_call(call: types.CallbackQuery):
    name = await get_filmname(call.data[12:])
    data_film=await search(name_film=name[1])
    ikb=await kb_films(name_films=int(call.data[12:]), user_id=call.from_user.id,type=data_film.type_kino_,id=data_film.id_)
    await bot.send_photo(chat_id=call.from_user.id, photo=data_film.photo_, caption=f'<b>🎥 {data_film.type_kino_}: </b><code>{data_film.name_film_}</code>\n\n🗓 Год производства: {data_film.year_}\n\n<b>👁 Жанры: {data_film.genre_}\n\n👥{data_film.text_autor_}: {data_film.director_}\n\n🔗 Длительность: {data_film.length_}мин</b>', reply_markup=ikb.row(types.InlineKeyboardButton('Назад🔙', callback_data='back_to_favorites')), parse_mode=types.ParseMode.HTML)
    
@dp.callback_query_handler(text='back_to_favorites')
async def back_to_favorites(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Ваш список избранных кино', reply_markup=await get_Favourites_kb(user_id=call.from_user.id))


@dp.callback_query_handler(IsinFavourites())
async def add_Favourites(call: types.CallbackQuery):
    msgcallme_data=call.get_current()
    await add_favourite(user_id=call.from_user.id, name=call.data[14:])
    ikb=types.InlineKeyboardMarkup()
    for i in msgcallme_data.message.reply_markup.inline_keyboard:
        if i[0]["text"] == 'В избранное🌟':
            i[0]["callback_data"]='delete_favourites_'+i[0]["callback_data"][14:]
            i[0]["text"]='Удалить из избранного🌟'
        ikb.row(i[0]) 
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=ikb)
    await call.answer('Добавлено в избранное🌟')

@dp.callback_query_handler(IsDeleteFavourites())
async def delete_Favourites(call: types.CallbackQuery):
    msgcallme_data=call.get_current()
    await delete_favourite(user_id=call.from_user.id, name=call.data[18:])
    ikb=types.InlineKeyboardMarkup()
    for i in msgcallme_data.message.reply_markup.inline_keyboard:
        if i[0]["text"] == 'Удалить из избранного🌟':
            i[0]["callback_data"]='in_favourites_'+i[0]["callback_data"][18:]
            i[0]["text"]='В избранное🌟'
        ikb.row(i[0]) 
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=ikb)
    await call.answer('Удалено из избранного🌟')
