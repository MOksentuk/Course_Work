class Manager:
    __liter_const = 1.1365
    __glass_const = 0.273
    __pint_const = 0.56826

    @staticmethod
    def checker(amount):
        """Проверка превышения максимально допустимого значения"""
        check_const = 2560
        if amount > check_const:
            return True

    @staticmethod
    def summator(*objects):
        ans = 0
        for obj in objects: ans += obj.amount
        return ans

    @staticmethod
    def decorator(value, name_1, name_2, name_3):
        """Расстановка окончаний в выводе в зависимости от значения"""
        ans = ''
        if 1 < abs(value % 10) < 5 or int(value) != value:
            ans += f'{value} {name_1}'
        elif abs(value) == 1:
            ans += f'{value} {name_2}'
        elif 4 < abs(value % 10) < 10 or value != 0:
            ans += f'{value} {name_3}'
        return ans

    def returner(self, value):
        """Перевод из литров в начальные меры объёма"""
        if value==0:
            return 'Полученное значение 0'
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

    def plus(self, lhs, rhs):
        """Сложение двух значений"""
        if self.checker(lhs.amount) or self.checker(rhs.amount):
            raise ValueError("Передано недопустимое значение")
        result = lhs.amount + rhs.amount
        if self.checker(result):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        return 'В полученном значении '+self.returner(result)

    def minus(self, lhs, rhs):
        """Вычитание двух значений"""
        if self.checker(lhs.amount) or self.checker(rhs.amount):
            raise ValueError("Передано недопустимое значение")
        result = lhs.amount - rhs.amount
        return 'В полученном значении '+self.returner(result)

    def comparison(self, lhs, rhs):
        """Сравнение двух значений"""
        if self.checker(lhs.amount) or self.checker(rhs.amount):
            raise ValueError("Переданное значение превышает максимально допустимое значение")
        result = abs(lhs.amount - rhs.amount)
        if lhs.amount > rhs.amount:
            return 'Первое значение больше второго на ' + self.returner(result)
        elif lhs.amount < rhs.amount:
            return 'Первое значение меньше второго на ' + self.returner(result)
        else:
            return 'Значения равны'

    def division_by_number(self, obj, const):
        """Деление на число"""
        if self.checker(obj.amount):
            raise ValueError("Переданное значение превышает максимально допустимое значение")
        result = obj.amount / const
        return 'В полученном значении '+self.returner(result)

    def multiplication_by_number(self, lhs, const):
        """Умножение на число"""
        result = lhs.amount * const
        if self.checker(result):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        return 'В полученном значении '+self.returner(result)

    def addition_to_max_value(self, obj):
        """Дополнение до максимального значения"""
        if self.checker(obj.amount):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        max_value = 256
        result = obj.amount - max_value
        return 'В полученном значении '+self.returner(result)

    def to_liter(self, obj):
        """Возвращение значения в литрах"""
        if self.checker(obj.amount):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        result = obj.amount * self.__liter_const
        ans = 'В полученном значении '
        return ans + self.decorator(result, 'литра', 'литр', 'литров')

    def to_glass(self, obj):
        """Перевод значения в стаканы"""
        if self.checker(obj.amount):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        result = obj.amount * self.__liter_const / self.__glass_const
        ans = 'В полученном значении '
        return ans + self.decorator(result, 'стакана', 'стакан', 'стаканов')

    def to_pint(self, obj):
        """Перевод значения в пинты"""
        if self.checker(obj.amount):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        result = obj.amount * self.__liter_const / self.__pint_const
        ans = 'В полученном значении '
        return ans + self.decorator(result, 'пинты', 'пинта', 'пинт')