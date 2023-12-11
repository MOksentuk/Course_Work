from Models.Quart import Quart
from Models.Gallon import Gallon
from Models.Bushel import Bushel
from Models.Storage import Storage


class Manager:

    @staticmethod
    def check_is_digit(amount):
        """Проверка на то, что значение является числом"""
        if amount != '':
            try:
                int(amount)
            except ValueError:
                return False

        return True

    @staticmethod
    def check_max_value(amount):
        """Проверка превышения максимально допустимого значения"""
        check_const = 2560

        if amount != '':
            return int(amount) <= check_const

    @staticmethod
    def check_negative(amount):
        """Проверка значения на неотрицательность"""

        if amount != '':
            return int(amount) >= 0

    @staticmethod
    def decorator(value, name_1, name_2, name_3) -> str:
        """Расстановка окончаний в выводе в зависимости от значения"""
        ans = ''
        if 4 < value < 21 or 4 < abs(value % 10) < 10 or value % 10 == 0:
            ans += f'{value} {name_3}'
        elif value % 10 == 1:
            ans += f'{value} {name_2}'
        elif 1 < abs(value % 10) < 5:
            ans += f'{value} {name_1}'

        return ans

    def inverter(self, value) -> str:
        """Перевод из литров в начальные меры объёма"""
        if value < 0:
            return 'полученное значение меньше нуля'
        elif value == 0:
            return '0'

        elif not self.check_max_value(value):
            return 'Превышено максимально допустимое значение'
        bushel_const = 32
        gallon_const = 4
        bushel = value // bushel_const
        gallon = (value % bushel_const) // gallon_const
        quart = value % bushel_const % gallon_const
        ans = ''
        if bushel != 0:
            ans += self.decorator(bushel, 'бушеля', 'бушель', 'бушелей')

        if gallon != 0:
            if bushel != 0:
                ans += ', '
            ans += self.decorator(gallon, 'галлона', 'галлон', 'галлонов')

        if quart != 0:
            if bushel != 0 or gallon != 0:
                ans += ', '
            ans += self.decorator(quart, 'кварты', 'кварта', 'кварт')

        return ans

    def init(self, name):
        """Инициализация составляющей члена операции или константы"""
        while True:
            amount = input(f'{name}: ')
            if amount == '':
                return 0
            if not self.check_is_digit(amount):
                print(f'Введено недопустимое значение, попробуйте ещё раз.\n')
                continue
            if not self.check_negative(amount):
                print(f'Введённое значение меньше 0, попробуйте ещё раз.\n')
                continue

            return int(amount)

    @staticmethod
    def number_of_operation():
        """Определение номера операции"""
        text = ('Выберите номер операции (для завершения работы просто нажмите Enter):\n'
                '1. Сложение\n'
                '2. Вычитание\n'
                '3. Сравнение\n'
                '4. Деление на число\n'
                '5. Умножение на число\n'
                '6. Дополнение до максимального значения\n'
                '7. Перевод в литры\n'
                '8. Перевод в стаканы\n'
                '9. Перевод в пинты\n>>> ')
        while True:
            number_of_operation = input(f'{text}')
            if number_of_operation == '':
                return False
            if number_of_operation in '123456789' and len(number_of_operation) == 1:
                return number_of_operation

            print(f'Переданное значение не может быть номером операции, '
                  'попробуйте ещё раз.\n')

    def term(self, ordinal):
        """Создание члена операции"""
        print(f'Введите значения {ordinal} члена операции в квартах, галлонах и бушелях'
              '\n(для того, чтобы пропустить значение, нажмите Enter):')
        while True:
            bushel = self.init('Бушели')
            gallon = self.init('Галлоны')
            quart = self.init('Кварты')
            term = Storage(Quart(quart), Gallon(gallon), Bushel(bushel))
            if self.check_max_value(term.amount):
                return term
            print('Введённое значение превышает максимально допустимое, '
                  'попробуйте ещё раз.')

    def comparison_processing(self, ans):
        """Обработка результатов операции "Сравнение\""""
        label = ans[0]
        amount = ans[1]
        if label is None:
            return 'значения равны'
        elif label:
            return f'первое значение больше второго на {self.inverter(amount)}'
        else:
            return f'первое значение меньше второго на {self.inverter(amount)}'

    def addition_to_max_value_processing(self, amount):
        """Обработка результатов операции "Дополнение до максимального значения\""""
        if amount:
            return f'до максимального значения не хватает {self.inverter(amount)}'
        else:
            return 'значение уже больше или равно максимальному'
