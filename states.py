from aiogram.fsm.state import State, StatesGroup

class MainState(StatesGroup):
    add_st = State()
    add_point = State()
    minus_point = State()


