from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from buttons import *
from states import MainState
from database.adminservice import *
# TODO id admina
admin_id = 305896408
group_id = -1002218282000
admin_router = Router()

@admin_router.message(Command(commands=["admin"]))
async def admin_mm(message: Message):
    if message.from_user.id == admin_id:
        await message.bot.send_message(message.from_user.id, f"🕵Панель админа\n",
                                       reply_markup=await admin_menu_in())
@admin_router.callback_query(F.data.in_(["cancel", "none",
                                         "add_student", "plus_points", "minus_points"]))
async def call_backs(query: CallbackQuery, state: FSMContext):
    await state.clear()
    if query.data == "cancel":
        await query.bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
        await state.clear()
    elif query.data == "none":
        pass
    elif query.data == "add_student":
        await query.bot.send_message(chat_id=query.from_user.id, text="Введи имя студента",
                                     reply_markup= await cancel_bt())
        await state.set_state(MainState.add_st)
    elif query.data == "plus_points":
        all_students = all_students_db()
        await query.bot.send_message(chat_id=query.from_user.id, text="Выбери студента для +репы",
                                     reply_markup=await students_in(all_students))
    elif query.data == "minus_points":
        all_students = all_students_db()
        await query.bot.send_message(chat_id=query.from_user.id, text="Выбери студента для -репы",
                                     reply_markup=await students_in(all_students))
        await state.set_data({"status": "minus"})
@admin_router.callback_query(F.data.in_(["being", "act", "hw", "bonus"]))
async def call_points(query: CallbackQuery, state: FSMContext):
    await query.bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
    if query.data == "being":
        await state.update_data({"category": "за присутствие на уроке"})
    elif query.data == "act":
        await state.update_data({"category": "за активность на уроке"})
    elif query.data == "hw":
        await state.update_data({"category": "за домашнюю работу"})
    elif query.data == "bonus":
        await state.update_data({"category": "в виде бонуса"})
    await query.bot.send_message(chat_id=query.from_user.id, text="Введи количество добавляемых поинтов",
                                 reply_markup=await cancel_bt())
    await state.set_state(MainState.add_point)


@admin_router.callback_query(lambda call: call.data in all_students_db())
async def get_for_what(query: CallbackQuery, state: FSMContext):
    name = query.data
    status = await state.get_data()
    await state.set_data({"name": name})
    if status == {}:
        await query.bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
        await query.bot.send_message(chat_id=query.from_user.id, text="Выбери категорию",
                                     reply_markup=await add_points_in())
    else:
        await query.bot.send_message(chat_id=query.from_user.id, text="Введи количество отнимаемых поинтов",
                                     reply_markup=await cancel_bt())
        await state.set_state(MainState.minus_point)






@admin_router.message(MainState.add_st)
async def get_add_student(message: Message, state: FSMContext):
    if message.text == "❌Отменить":
        await message.bot.send_message(message.from_user.id, "🚫Действие отменено", reply_markup=await main_menu_bt())
        await state.clear()
    elif message.text:
        try:
            add_student_db(message.text)
            await message.bot.send_message(message.from_user.id, "Ученик добавлен")
            await state.clear()
        except:
            await message.bot.send_message(message.from_user.id, "️️❗Не удалось")
            await state.clear()
    else:
        await message.bot.send_message(message.from_user.id, "️️❗Неправильный формат")
        await state.clear()
@admin_router.message(MainState.add_point)
async def add_point(message: Message, state: FSMContext):
    if message.text == "❌Отменить":
        await message.bot.send_message(message.from_user.id, "🚫Действие отменено", reply_markup=await main_menu_bt())
        await state.clear()
    elif message.text:
        try:
            all_data = await state.get_data()
            name = all_data.get("name")
            category = all_data.get("category")
            add_points_db(name, message.text)
            await message.bot.send_message(message.from_user.id, "Репутация добавлена")
            await message.bot.send_message(group_id, f"📈️{name} получил {message.text} репы {category}")
            await state.clear()
        except:
            await message.bot.send_message(message.from_user.id, "️️❗Не удалось")
            await state.clear()
    else:
        await message.bot.send_message(message.from_user.id, "️️❗Неправильный формат")
        await state.clear()
@admin_router.message(MainState.add_point)
async def minus_point(message: Message, state: FSMContext):
    if message.text == "❌Отменить":
        await message.bot.send_message(message.from_user.id, "🚫Действие отменено", reply_markup=await main_menu_bt())
        await state.clear()
    elif message.text:
        try:
            all_data = await state.get_data()
            name = all_data.get("name")
            minus_points_db(name, message.text)
            await message.bot.send_message(message.from_user.id, "Репутация добавлена")
            await message.bot.send_message(group_id, f"📉{name} потерял {message.text} репы")
            await state.clear()
        except:
            await message.bot.send_message(message.from_user.id, "️️❗Не удалось")
            await state.clear()
    else:
        await message.bot.send_message(message.from_user.id, "️️❗Неправильный формат")
        await state.clear()
@admin_router.message(F.text=="❌Отменить")
async def profile(message: Message, state: FSMContext):
    await message.bot.send_message(message.from_user.id, "️️Все действия отменены", reply_markup=await main_menu_bt())
    await state.clear()
