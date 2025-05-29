from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from buttons import *
from database.userservice import *
from datetime import datetime
import pytz

bot_router = Router()
group_id = -1002218282000
@bot_router.message(CommandStart())
async def start(message: Message):
    await message.bot.send_message(message.from_user.id, "Приветствую в боте душителей питона."
                                                         "Выбери действие в меню.",
                                   reply_markup=await main_menu_bt())
@bot_router.message(F.text=="📊Рейтинг")
async def rating(message: Message):
    tashkent_timezone = pytz.timezone('Asia/Tashkent')
    all_info = all_rating_db()
    time = datetime.now(tashkent_timezone).strftime("%Y-%m-%d")
    text = f"📊Актуальный рейтинг 💅 за  {time}:\n"
    count = 1
    for i in all_info:
        text += f"\n<b>{count}. {i[0]}</b>  {i[1]}"
        count +=1
    await message.bot.send_message(message.chat.id, text=text, parse_mode="html", reply_markup= await main_menu_bt())
@bot_router.message(F.text=="💳Карта препода")
async def donate(message: Message):
    await message.bot.send_message(message.chat.id, text="Принимаются донаты на еду и такси преподу🧌\n"
                                                         "<code>8600570404948787</code>\n\n"
                                                         "ps.они никак повлияют на ваши очки репутации",
                                   parse_mode="html", reply_markup=await main_menu_bt())