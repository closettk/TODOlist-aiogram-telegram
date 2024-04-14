from aiogram import F, types, Router
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.keyboards import start_kb, yesorno_kb, howmuch_kb , h2_kb, h3_kb, h4_kb, h5_kb, obratno, task_detail_kb
from db import add_task, get_tasks, get_task_detail, delete_task, mark_task_as_completed, get_completed_tasks
from aiogram.types import FSInputFile
from aiogram import Router, types
from aiogram.filters import Command

from handlers.handlers import display_tasks

router = Router()

async def display_completed_tasks(callback_or_message, state: FSMContext):
    if isinstance(callback_or_message, types.CallbackQuery):
        user_id = str(callback_or_message.from_user.id)
        message = callback_or_message.message
    else:
        user_id = str(callback_or_message.from_user.id)
        message = callback_or_message

    completed_tasks = await get_completed_tasks(user_id)
    buttons = [[
        InlineKeyboardButton(text='Вернуться в меню ◀️', callback_data='back_to_tasks')
    ]]

    if completed_tasks:
        for task in completed_tasks:
            task_button = InlineKeyboardButton(text=task[1], callback_data=f"completed_task_{task[0]}")
            buttons.append([task_button])

    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.edit_text("Выполненные задачи:", reply_markup=kb)

@router.callback_query(F.data == 'back_to_tasks')
async def backtomenu(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Меню:',reply_markup=start_kb())

@router.callback_query(F.data == 'history')
async def show_history(callback: types.CallbackQuery, state: FSMContext):
    await display_completed_tasks(callback, state,)


