from aiogram.fsm.state import State, StatesGroup
import numpy as np
import pandas as pd

class Foydalanuvchi(StatesGroup):
    familya = State()
    ism = State()


def salom(fm, im):
    salomlar = f'Assolomu alaykum {fm} {im}'
    return salomlar

def baza(fm, im):
    """Bunda familya ism olib exeldan malumot qaytaradi"""
    data = pd.read_excel('baza.xlsx')
    df = pd.DataFrame(data)  
    df1 = df[df['Candidate first name']== im ]
    df2 = df1[df1['Candidate last name']== fm]
    imtihonlar = df2.values   
        
    return imtihonlar

