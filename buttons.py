from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
async def main_menu_bt():
    buttons = [
        [KeyboardButton(text="📊Рейтинг"),],
        [KeyboardButton(text="💳Карта препода")]
        ]
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=buttons)
    return kb

async def cancel_in():
    buttons = [
        [InlineKeyboardButton(text="❌Отменить", callback_data="cancel")]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
async def link_in():
    buttons = [
        [InlineKeyboardButton(text="↩️Не менять ссылку", callback_data="cancel")]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

async def admin_menu_in():
    buttons = [
        [InlineKeyboardButton(text="Добавить ученика", callback_data="add_student")],
        [InlineKeyboardButton(text="Добавить баллы", callback_data="plus_points")],
        [InlineKeyboardButton(text="Отнять баллы", callback_data="minus_points")],
        [InlineKeyboardButton(text="Закрыть", callback_data="cancel")]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
async def students_in(all_students):
    keyboard_builder = InlineKeyboardBuilder()
    for i in all_students:
        try:
            keyboard_builder.button(text=i, callback_data=i)
        except:
            pass
    keyboard_builder.button(text="Закрыть", callback_data="cancel")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
async def add_points_in():
    buttons = [
        [InlineKeyboardButton(text="Присутствие", callback_data="being")],
        [InlineKeyboardButton(text="Активность", callback_data="act")],
        [InlineKeyboardButton(text="Домашка", callback_data="hw")],
        [InlineKeyboardButton(text="Бонус", callback_data="bonus")],
        [InlineKeyboardButton(text="Закрыть", callback_data="cancel")]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb
async def cancel_bt():
    buttons = [
        [KeyboardButton(text="❌Отменить")]
    ]
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=buttons)
    return kb