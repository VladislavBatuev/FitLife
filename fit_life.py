import sys
import const as ct # Были добавлены константы через сторонний файл

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

def greetings():
    """Обрабатывает ввод имени и возраста пользователя."""
    user_name = input('Введите своё имя пользователя: ')
    user_name = user_name.title()
    user_age = int(input('Теперь просим ввести возраст пользователя: '))
    print('-' * ct.LINING)
    return user_name, user_age


def bmi_calc():
    """Рассчитывает ИМТ и норму воды."""
    user_weight = input('Введите ваш вес(кг): ')
    user_weight = float(user_weight.replace(',', '.'))  # Вместо просьбы о не использовании запятых был использован не совсем знакомый метод replace
    user_height = input('Введите ваш рост(м): ')
    user_height = float(user_height.replace(',', '.'))
    bmi = user_weight / (user_height ** 2)
    bmi = round(bmi, 1)
    water_ml = user_weight * ct.NORMAL_NUMBER
    water_l = water_ml / ct.CONVERSION
    water_l = round(water_l, 2)
    return bmi, water_l


print('\nДобро пожаловать! Вас приветствует FitLife!')
name, age = greetings()
bmi, water = bmi_calc()
print('-' * ct.LINING)
print('\n' + '=' * ct.SUB_LINING)
print('ВАШ ОТЧЁТ')
print('=' * ct.SUB_LINING)
print(f'Имя: {name}')
print(f'Возраст: {age}')
print(f'ИМТ: {bmi}')
print(f'Ваша норма воды составляет: {water}')
print('-' * ct.LINING)
print('Расчёт окончен. Будьте здоровы!')
