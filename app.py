from aiogram import executor, types
from aiogram.dispatcher import FSMContext
from loader import dp, bot, admin_id
from handlers import dp
from keybord_s.ohter import ikb_close
from keybord_s.user import kb_user

#отмена любого состаяния#
@dp.callback_query_handler(text='cancellation_state', state='*')
async def cancellation_state(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer('Отмена❌')
    await call.message.delete()
    
#закрыть#
@dp.callback_query_handler(text='close_text')
async def cancellation_state(call: types.Message):
    await call.message.delete()

@dp.message_handler()
async def empty_command(message: types.Message):
    await message.delete()
    await message.answer('Такой команды нет🖍', reply_markup=await kb_user(message.from_user.id))

executor.start_polling(dp)