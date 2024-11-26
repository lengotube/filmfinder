from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,\
                          ReplyKeyboardMarkup, KeyboardButton
from data.db import get_AllChennel, get_Allplayer, get_UserFavouritesWfilm, get_UserAllFavourites, get_filmname
from misc.search_film import search
from .ohter import ikb_close_oikb
import config

async def kb_user(user_id):
    kb_user=ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb_user.row('Поиск🔍')
    kb_user.insert('Избранное🌟')
    if user_id in config.admin_id:
        kb_user.insert('Админ меню')
    return kb_user

kb_back=ReplyKeyboardMarkup(resize_keyboard=True)
kb_back.row('Отмена❌')

async def get_Favourites_kb(user_id):
    ikb=InlineKeyboardMarkup(row_width=1)
    #[(1350162917, 'Уэнсдэй'), (1350162917, 'Томирис')]
    data_Favourites_user=await get_UserAllFavourites(user_id=user_id)
    for i in data_Favourites_user:
        name = await get_filmname(i[1])
        ikb.row(InlineKeyboardButton(name[1]+'🌟', callback_data='search_film_'+str(i[1])))
    ikb.row(ikb_close_oikb)
    return ikb
        
#получения листа о подписках#
async def sub_list():
    data_chennel=await get_AllChennel()
    sub_list=InlineKeyboardMarkup(row_width=1)
    for i in data_chennel:
        sub_list.add(InlineKeyboardButton(text=i[1], url=i[2]))
    sub_list.add(InlineKeyboardButton(text='Одна из сыллок не работает❓', callback_data='link_no_work'))
    return sub_list

#кнопки для просмотра кино с бесплатным плеером#
async def kb_films(name_films, user_id, type, id):
    name_films = str(name_films)
    ikb=InlineKeyboardMarkup(row_width=1)
    for i in await get_Allplayer():
        if i[2]:
            try:
                name = await get_filmname(int(name_films))
                ikb.row(InlineKeyboardButton(text=i[3], url=f'{i[0]}/{"film" if type == "Фильм" else "series"}/{id}'))
            except Exception as ex:
                print(ex)
                pass

    if await get_UserFavouritesWfilm(user_id=user_id, name=name_films) == []:
        ikb.row(InlineKeyboardButton('В избранное🌟', callback_data='in_favourites_'+name_films))
    else:
        ikb.row(InlineKeyboardButton('Удалить из избранного🌟', callback_data='delete_favourites_'+name_films))
    ikb.row(ikb_close_oikb)
    return ikb