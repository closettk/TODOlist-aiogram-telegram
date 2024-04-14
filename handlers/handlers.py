from aiogram import F, types, Router
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.keyboards import start_kb, task_detail_kb
from db import add_task, get_tasks, get_task_detail
from aiogram.types import FSInputFile
from aiogram import Router, types
from aiogram.filters import Command

creator = 6130402432
router = Router()

#делает inline клавиатуру со списком задач
async def display_tasks(callback_or_message, state: FSMContext, TEXT):
    if isinstance(callback_or_message, types.CallbackQuery):
        user_id = str(callback_or_message.from_user.id)
        message = callback_or_message.message
    else:
        user_id = str(callback_or_message.from_user.id)
        message = callback_or_message
    
    tasks = await get_tasks(user_id)
    # Добавляем кнопку "Вернуться" на ту же строку, что и кнопка "Добавить задачу ➕"
    buttons = [[
        InlineKeyboardButton(text='Добавить задачу 📝', callback_data='add'),
        InlineKeyboardButton(text='Вернуться ◀️', callback_data='back')  # Добавляем кнопку "Вернуться"
    ]]

    if tasks:
        task_buttons = [InlineKeyboardButton(text=task[1], callback_data=f"task_{task[0]}") for task in tasks]
        buttons.extend([[button] for button in task_buttons])

    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.edit_text(f"{TEXT}", reply_markup=kb)


@router.message(F.text == '/start')
async def start_co(message: types.Message):
    await message.answer('Меню:',reply_markup=start_kb())

#кнопка назад
@router.callback_query(F.data == 'back')
async def go_back(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Меню:", reply_markup=start_kb())
    await state.clear()  # Очищаем состояние, если необходимо
#еще одна кнопка назад
@router.callback_query(F.data == 'back2')
async def go_back2(callback: types.CallbackQuery, state: FSMContext):
    TEXT = "Ваши задачи:"
    await display_tasks(callback, state, TEXT=TEXT)
    await state.clear()  # Очищаем состояние, если необходимо

#кнопка посмотреть задачи
@router.callback_query(F.data == "check")
async def show_tasks(callback: types.CallbackQuery, state: FSMContext):
    TEXT = "Ваши задачи:"
    await display_tasks(callback, state, TEXT=TEXT)
