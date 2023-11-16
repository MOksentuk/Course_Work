class Manager:
    @staticmethod
    def check_is_digit(amount):
        if amount != '':
            if not str(amount).isdigit():
                raise ValueError("Передано недопустимое значение")

    @staticmethod
    def check_max_value(amount):
        """Проверка допустимого значения"""
        check_const = 2560

        if amount != '':
            if abs(float(amount)) > check_const:
                raise ValueError("Передано недопустимое значение")

    @staticmethod
    def decorator(value, name_1, name_2, name_3) -> str:
        """Расстановка окончаний в выводе в зависимости от значения"""
        ans = ''
        if 1 < abs(value % 10) < 5 or int(value) != value:
            ans += f'{value} {name_1}'
        elif abs(value) == 1:
            ans += f'{value} {name_2}'
        elif 4 < abs(value % 10) < 10 or value != 0:
            ans += f'{value} {name_3}'
        return ans

    def returner(self, value) -> str:
        """Перевод из литров в начальные меры объёма"""
        if value == 0:
            return 'Полученное значение равно 0'
        self.check_max_value(value)
        bushel_const = 32
        gallon_const = 4
        bushel = value // bushel_const
        gallon = (value % bushel_const) // gallon_const
        quart = value % bushel_const % gallon_const
        ans = ''
        ans += self.decorator(bushel, 'бушеля', 'бушель', 'бушелей')

        if bushel != 0 and gallon != 0:
            ans += ', '
        ans += self.decorator(gallon, 'галлона', 'галлон', 'галлонов')

        if quart != 0 and gallon != 0:
            ans += ', '
        ans += self.decorator(quart, 'кварты', 'кварта', 'кварт')

        return ans