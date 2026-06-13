import sys


sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

def greetings():  # функция обрабатывающая Имя и Возраст
    user_name = input('Введите своё имя пользователя: ')
    user_name = user_name.title()
    user_age = int(input('Теперь просим ввести возраст пользователя: '))
    print('-' * 45)
    return user_name, user_age


def bmi_calc():  # функция для расчётов
    print('Просим вводить следующие значения через точку (например, рост(м): 1.82)')
    print()
    user_weight = float(input('Введите ваш вес(кг): '))
    user_height = float(input('Введите ваш рост(м): '))
    bmi = user_weight / (user_height ** 2)  # расчёт индекса массы тела
    bmi = round(bmi, 1)
    water_ml = user_weight * 30
    water_l = water_ml / 1000
    water_l = round(water_l, 2)
    return bmi, water_l

print('\nДобро пожаловать! Вас приветствует FitLife!')
name, age = greetings()
bmi, water = bmi_calc()
print('-' * 45)
print('\n' + '=' * 35)
print('ВАШ ОТЧЁТ')
print('=' * 35)
print(f'Имя: {name}') 
print(f'Возраст: {age}') 
print(f'ИМТ: {bmi}')
print(f'Ваша норма воды составляет: {water}')
print('-' * 45)
print('Расчёт окончен. Будьте здоровы!')