from aiogram.fsm.state import State, StatesGroup
import numpy as np
import pandas as pd

class Foydalanuvchi(StatesGroup):
    familya = State()
    ism = State()


def salom(fm, im):
    salomlar = f'Assolomu alaykum {fm} {im}'
    return salomlar

