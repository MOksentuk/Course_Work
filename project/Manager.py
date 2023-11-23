class Manager:
    @staticmethod
    def check_is_digit(amount):
        if amount != '':
            try:
                float(amount)
            except ValueError:
                return False
            return True

    @staticmethod
    def check_max_value(amount):
        """Проверка допустимого значения"""
        check_const = 2560

        if amount != '':
            if abs(float(amount)) > check_const or float(amount) < 0:
                return False
            return True

    @staticmethod
    def decorator(value, name_1, name_2, name_3) -> str:  # можно вынести в отдельный файл
        """Расстановка окончаний в выводе в зависимости от значения"""
        ans = ''
        if 1 < abs(value % 10) < 5 or int(value) != value:
            ans += f'{value} {name_1}'
        elif abs(value) == 1:
            ans += f'{value} {name_2}'
        elif 4 < abs(value % 10) < 10 or value != 0:
            ans += f'{value} {name_3}'
        return ans

    def inverter(self, value) -> str:  # можно разбить на два класса
        """Перевод из литров в начальные меры объёма"""
        if value < 0:
            return 'Полученное значение меньше нуля'
        elif value == 0:
            return 'Полученное значение равно 0'

        self.check_max_value(value)
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

    def init(self, name):
        amount = input(f'{name}: ')
        while True:
            if not self.check_is_digit(amount):
                amount = input(f'Введено недопустимое значение.\n{name}: ')
                continue
            if not self.check_max_value(amount):
                amount = input(f'Введённое значение превышает максимально допустимое.\n{name}: ')
                continue
            break

        return amount

    def comparison_processing(self, ans):
        label = ans[0]
        amount = ans[1]
        if amount is None:
            return 'Значения равны'
        elif label:
            return f'Первое значение больше второго на {self.inverter(amount)}'
        else:
            return f'Первое значение меньше второго на {self.inverter(amount)}'


        return ans
