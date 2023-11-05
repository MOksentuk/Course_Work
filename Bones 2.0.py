class Manager:
    @staticmethod
    def checker(amount):
        """Проверки превышения максимально допустимого значения"""
        check_const = 2909.4

        return amount > check_const

    @staticmethod
    def getter(value):
        """Перевод из литров в начальные меры объёма"""
        bushel_const = 36.368
        gallon_const = 4.546
        quart_const = 1.1365
        bushel = str(value // bushel_const)
        gallon = (value % bushel_const) // gallon_const
        quart = (value % bushel_const % gallon_const) // quart_const
        ans = 'В полученном значении '
        if bushel[-1] == '1':
            ans += bushel + ' бушель'
        elif bushel[-1] in '234':
            ans += bushel + ' бушелей'  # (1) бушель, (2-4) бушеля, (5-9) бушелей
        elif bushel[-1] in '56789' or bushel != '0.0':
            ans += bushel + ' бушелей'
        if bushel != '0.0' and gallon != 0:
            ans += ', '
        if gallon == 1:
            ans += str(gallon) + ' галлон'  # 1 кварта, 2-3 кварты
        elif 1 < gallon < 5:
            ans += str(gallon) + ' галлона'
        elif 4 < gallon < 8:
            ans += str(gallon) + ' галлонов'  # 1 галлон, 2-4 галлона, 5-7 галлонов
        if quart != 0 and gallon != 0:
            ans += ', '
        if quart == 1:
            ans += str(quart) + ' кварта'  # 1 кварта, 2-3 кварты
        elif 1 < quart < 4:
            ans += str(quart) + ' кварты'
        return ans + '.'

    def plus(self, lhs, rhs):
        """Сложение двух значений"""
        if self.checker(lhs.amount) or self.checker(rhs.amount):
            raise ValueError("Переданное значение превышает максимально допустимое значение")
        result = lhs.amount + rhs.amount
        if self.checker(result):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        return self.getter(result)

    def minus(self, lhs, rhs):
        """Вычитание двух значений"""
        if self.checker(lhs.amount) or self.checker(rhs.amount):
            raise ValueError("Переданное значение превышает максимально допустимое значение")
        result = lhs.amount - rhs.amount
        return self.getter(result)

    def comparison(self, lhs, rhs):
        """Сравнение двух значений"""
        if self.checker(lhs.amount) or self.checker(rhs.amount):
            raise ValueError("Переданное значение превышает максимально допустимое значение")
        result = abs(lhs.amount - rhs.amount)
        if lhs > rhs:
            return 'Первое значение больше второго на', result.getter
        elif lhs < rhs:
            return 'Первое значение меньше второго на', result.getter
        else:
            return 'Значения равны'

    def division_by_number(self, obj, const):
        """Деление на число"""
        if self.checker(obj.amount):
            raise ValueError("Переданное значение превышает максимально допустимое значение")
        result = obj.amount / const
        return self.getter(result)

    def multiplication_by_number(self, lhs, const):
        """Умножение на число"""
        result = lhs.amount * const
        if self.checker(result):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        return self.getter(result)

    def addition_to_max_value(self, lhs, rhs):
        """Дополнение до максимального значения"""
        result = lhs.amount + rhs.amount
        if self.checker(result):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        return self.getter(result)

    def to_liter(self, obj):
        """Возвращение значения в литрах"""
        if self.checker(obj.amount):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        return obj.amount

    def to_glass(self, obj):
        """Перевод значения в стаканы"""
        const = 0.273
        if self.checker(obj.amount):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        return obj.amount / const

    def to_pint(self, obj):
        """Перевод значения в пинты"""
        const = 0.56826
        if self.checker(obj.amount):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        return obj.amount / const


class Quart:
    const = 1.1365

    def __init__(self, amount):
        self.amount = amount * self.const


class Gallon:
    const = 4.546

    def __init__(self, amount):
        self.amount = amount * self.const


class Bushel:
    const = 36.368

    def __init__(self, amount):
        self.amount = amount * self.const


q1 = Quart(11)
# g1 = Gallon(23)
q2 = Quart(16)
# c1 = Bushel(2)
# c2 = Bushel(3)

manager = Manager()
print(manager.plus(q2, q1))
# print(manager.plus(c2, c1))
# print(manager.to_glass(q1))
# print(manager.to_liter(q1))
print(manager.division_by_number(q1, 4))
