from application.salary import calculate_salary
from application.db.people import get_employees

from datetime import datetime

from art import text2art, aprint


def text_to_image(text):
    # Функция создает из переданого текста (Eng) изображение используя символы ASCII
    # и печатает результат
    print(text2art(text))

def draw_random():
    # Функция печатает случайный смайлик/изображение символами ASCII
    aprint('random')

if __name__=='__main__':
    print('Текущая дата:',datetime.now().date())
    calculate_salary()
    get_employees()

    text_to_image('ALIEN')
    draw_random()