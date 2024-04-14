from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_kb() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Посмотреть задачи 🗄', callback_data='check')],
        [InlineKeyboardButton(text='Выполенные задачи ✅', callback_data='history')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def completed_task_detail_kb(task_id) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Удалить ❌', callback_data=f'delete_completed_{task_id}'),
        InlineKeyboardButton(text='Назад ◀️', callback_data='back_to_completed')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def task_detail_kb() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Выполнено ✅', callback_data='success'),
        InlineKeyboardButton(text='Не выполнено ❌', callback_data='fail')],
        [InlineKeyboardButton(text='Назад ◀️', callback_data='back2')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)  # По 2 кнопки в ряд для удобства
    return kb

def obratno() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Назад ◀️', callback_data='back2')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)  # По 2 кнопки в ряд для удобства
    return kb


def yesorno_kb() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Да ✅', callback_data='yes'),
         InlineKeyboardButton(text='Нет ❌', callback_data='no')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def howmuch_kb() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='⭐️',callback_data='one'),
         InlineKeyboardButton(text='🌑',callback_data='two'),
         InlineKeyboardButton(text='🌑',callback_data='three'),
         InlineKeyboardButton(text='🌑',callback_data='four'),
         InlineKeyboardButton(text='🌑',callback_data='five')],
         [InlineKeyboardButton(text='Потвердить ✅', callback_data='yes2'),
         InlineKeyboardButton(text='Отменить ❌', callback_data='no2')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def h2_kb() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='⭐️',callback_data='one'),
         InlineKeyboardButton(text='⭐️',callback_data='two'),
         InlineKeyboardButton(text='🌑',callback_data='three'),
         InlineKeyboardButton(text='🌑',callback_data='four'),
         InlineKeyboardButton(text='🌑',callback_data='five')],
         [InlineKeyboardButton(text='Потвердить ✅', callback_data='yes2'),
         InlineKeyboardButton(text='Отменить ❌', callback_data='no2')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def h3_kb() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='⭐️',callback_data='one'),
         InlineKeyboardButton(text='⭐️',callback_data='two'),
         InlineKeyboardButton(text='⭐️',callback_data='three'),
         InlineKeyboardButton(text='🌑',callback_data='four'),
         InlineKeyboardButton(text='🌑',callback_data='five')],
         [InlineKeyboardButton(text='Потвердить ✅', callback_data='yes2'),
         InlineKeyboardButton(text='Отменить ❌', callback_data='no2')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def h4_kb() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='⭐️',callback_data='one'),
         InlineKeyboardButton(text='⭐️',callback_data='two'),
         InlineKeyboardButton(text='⭐️',callback_data='three'),
         InlineKeyboardButton(text='⭐️',callback_data='four'),
         InlineKeyboardButton(text='🌑',callback_data='five')],
         [InlineKeyboardButton(text='Потвердить ✅', callback_data='yes2'),
         InlineKeyboardButton(text='Отменить ❌', callback_data='no2')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def h5_kb() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='⭐️',callback_data='one'),
         InlineKeyboardButton(text='⭐️',callback_data='two'),
         InlineKeyboardButton(text='⭐️',callback_data='three'),
         InlineKeyboardButton(text='⭐️',callback_data='four'),
         InlineKeyboardButton(text='⭐️',callback_data='five')],
         [InlineKeyboardButton(text='Потвердить ✅', callback_data='yes2'),
         InlineKeyboardButton(text='Отменить ❌', callback_data='no2')]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb