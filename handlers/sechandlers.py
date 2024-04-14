#здесь реализуется выбор сложности задачи. В кратце: при нажатии на 1 появляется inline клавиатура
#где только одна звезда, при нажатии на 5 открывается клавиатура со всеми звездами
from aiogram import F, types, Router
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.keyboards import start_kb, yesorno_kb, howmuch_kb , h2_kb, h3_kb, h4_kb, h5_kb, obratno, task_detail_kb, completed_task_detail_kb
from db import add_task, get_tasks, get_task_detail, delete_task, mark_task_as_completed
from aiogram.types import FSInputFile
from aiogram import Router, types
from aiogram.filters import Command

from handlers.handlers import display_tasks
from handlers.thirdhandlers import display_completed_tasks

class SomeState(StatesGroup):
    wait1 = State()
    wait_difficulty = State()

router = Router()

@router.callback_query(F.data == "add")
async def add_co(callback: types.CallbackQuery, state: FSMContext):
    print('sdfdsfds')
    await callback.message.edit_text('Напишите вашу задачу', reply_markup=obratno())
    await state.set_state(SomeState.wait1)

@router.message(SomeState.wait1)
async def waitfortext(message: types.Message, state: FSMContext):
    await state.update_data(task_text=message.text)
    await message.answer(f"{message.text}\nВерно?", reply_markup=yesorno_kb())

@router.callback_query(F.data == "no")
async def cancel_task(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Добавление задачи отменено", reply_markup=start_kb())
    await state.clear()

@router.callback_query(F.data == "yes")
async def confirm_task(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    await callback.message.edit_text("Оцените сложность задачи\nот 1 до 5", reply_markup=howmuch_kb())
    # Сохраняем текст задачи для дальнейшего использования
    await state.update_data(task_text=user_data['task_text'])
    await state.update_data(difficulty=1)
    # Переходим в новое состояние для ожидания выбора сложности
    await state.set_state(SomeState.wait_difficulty)

@router.callback_query(F.data == 'one')
async def handle_one(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    current_difficulty = user_data.get('difficulty')  # Значение по умолчанию не требуется

    if current_difficulty != 1:
        await state.update_data(difficulty=1)
        await callback.message.edit_text("Оцените сложность задачи\nот 1 до 5", reply_markup=howmuch_kb())
    else:
        pass

@router.callback_query(F.data == 'two')
async def handle_two(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    current_difficulty = user_data.get('difficulty')  # Значение по умолчанию не требуется

    if current_difficulty != 2:
        await state.update_data(difficulty=2)
        await callback.message.edit_text("Оцените сложность задачи\nот 1 до 5", reply_markup=h2_kb())
    else:
        pass

@router.callback_query(F.data == 'three')
async def handle_three(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    current_difficulty = user_data.get('difficulty')  # Значение по умолчанию не требуется

    if current_difficulty != 3:
        await state.update_data(difficulty=3)
        await callback.message.edit_text("Оцените сложность задачи\nот 1 до 5", reply_markup=h3_kb())
    else:
        pass

@router.callback_query(F.data == 'four')
async def handle_four(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    current_difficulty = user_data.get('difficulty')  # Значение по умолчанию не требуется

    if current_difficulty != 4:
        await state.update_data(difficulty=4)
        await callback.message.edit_text("Оцените сложность задачи\nот 1 до 5", reply_markup=h4_kb())
    else:
        pass

@router.callback_query(F.data == 'five')
async def handle_five(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    current_difficulty = user_data.get('difficulty')  # Значение по умолчанию не требуется

    if current_difficulty != 5:
        await state.update_data(difficulty=5)
        await callback.message.edit_text("Оцените сложность задачи\nот 1 до 5", reply_markup=h5_kb())
    else:
        pass

@router.callback_query(F.data == "yes2")
async def confirm_difficulty(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    difficulty = user_data.get('difficulty')  # По умолчанию сложность равна 1
    task_text = user_data['task_text']
    await add_task(str(callback.from_user.id), task_text, difficulty)
    TEXT = f"Добавлена задача со сложностью {str(difficulty)}\nВаши задачи:"
    await display_tasks(callback, state, TEXT=TEXT)
    await state.clear()

@router.callback_query(F.data == "no2")
async def cancelhowmuch(callback: types.CallbackQuery, state: FSMContext):
    TEXT = 'Задача не сохранилась\nВаши задачи:'
    await display_tasks(callback, state, TEXT=TEXT)  # Переиспользование функции вывода задач
    await state.clear()

@router.callback_query()
async def callback_query_handler(callback: types.CallbackQuery, state: FSMContext):
    data = callback.data

    if data.startswith('task_'):
        task_id = int(data.split('_')[1])
        await state.update_data(task_id=task_id)  # Сохраняем ID задачи в состояние
        task = await get_task_detail(task_id)
        
        if task:
            message_text = f"Задача: {task['task_text']}\nСложность: {'⭐️' * task['difficulty']}\nНачата: {task['created_at']}"
            await callback.message.edit_text(message_text, reply_markup=task_detail_kb())
        else:
            await callback.message.edit_text("Задача не найдена.")
    elif data == 'success':
        # Выполнено
        user_data = await state.get_data()
        task_id = user_data.get('task_id')
        if task_id:
            await mark_task_as_completed(task_id)
            await callback.answer("Задача помечена как выполненная")
            TEXT = f"Задача помечена как выполненная\nВаши задачи:"
            await display_tasks(callback, state, TEXT=TEXT)
    elif data == 'fail':
        # Не выполнено
        user_data = await state.get_data()
        task_id = user_data.get('task_id')
        if task_id:
            await delete_task(task_id)
            TEXT = f"Задача удалена\nВаши задачи:"
            await display_tasks(callback, state, TEXT=TEXT)
    elif data.startswith('completed_task_'):
        task_id = int(data.split('_')[2])
        task = await get_task_detail(task_id)
        
        if task:
            message_text = f"""Задача: {task['task_text']}
    Сложность: {'⭐️' * task['difficulty']}
    Начата: {task['created_at']}
    Завершена: {task['completed_at']}
    Длительность выполнения: {task['duration']}"""
            await callback.message.edit_text(message_text, reply_markup=completed_task_detail_kb(task_id))
        else:
            await callback.message.edit_text("Задача не найдена.")

    elif data == 'back_to_completed':
        await display_completed_tasks(callback, state)

    elif data.startswith('delete_completed_'):
        task_id = int(data.split('_')[2])
        await delete_task(task_id)  # Убедитесь, что у вас есть функция для удаления задачи
        await callback.answer("Задача удалена")
        await display_completed_tasks(callback, state)  # Возвращаем пользователя к списку выполненных задач
    elif data == 'back_to_completed':
        await display_completed_tasks(callback, state)