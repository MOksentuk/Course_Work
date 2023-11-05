class Manager:
    @staticmethod
    def checker(amount):
        """Проверки превышения максимально допустимого значения"""
        check_const = 2560

        return amount > check_const



    @staticmethod
    def getter(value):
        """Перевод из литров в начальные меры объёма"""
        bushel_const = 32
        gallon_const = 4
        bushel = value // bushel_const
        gallon = (value % bushel_const) // gallon_const
        quart = value % bushel_const % gallon_const
        ans = 'В полученном значении '
        if 1 < bushel % 10 < 5:
            ans += f'{bushel} бушеля'  # (1) бушель, (2-4) бушеля, (5-9) бушелей
        elif bushel == 1:
            ans += f'{bushel} бушель'
        elif 4 < bushel % 10 < 10 or bushel != 0:
            ans += f'{bushel} бушелей'

        if bushel != 0 and gallon != 0: ans += ', '

        if 1 < gallon % 10 < 5:
            ans += f'{gallon} галлона'  # (1) бушель, (2-4) бушеля, (5-9) бушелей
        elif gallon == 1:
            ans += f'{gallon} галлон'
        elif 4 < gallon % 10 < 10 or gallon != 0:
            ans += f'{gallon} галлонов'
        if quart != 0 and gallon != 0: ans += ', '
        if 1 < quart % 10 < 4 or int(quart) != quart:
            ans += f'{quart} кварты'  # (1) бушель, (2-4) бушеля, (5-9) бушелей
        elif quart == 1:
            ans += f'{quart} кварта'
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
        result = obj.amount * obj.liter_const
        ans = 'В полученном значении '
        return ans

    def to_glass(self, obj):
        """Перевод значения в стаканы"""
        const = 0.273
        if self.checker(obj.amount):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        return self.to_liter(obj) / const

    def to_pint(self, obj):
        """Перевод значения в пинты"""
        const = 0.56826
        if self.checker(obj.amount):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        return self.to_liter(obj) / const


class Quart:
    liter_const = 1.1365

    def __init__(self, amount):
        self.amount = amount


class Gallon:
    liter_const = 4.546
    quart_const = 4

    def __init__(self, amount):
        self.amount = amount * self.quart_const


class Bushel:
    liter_const = 36.368
    quart_const = 32

    def __init__(self, amount):
        self.amount = amount * self.quart_const


q1 = Quart(11)
# g1 = Gallon(23)
q2 = Quart(16)
c1 = Bushel(20)
c2 = Bushel(3)

manager = Manager()
print(manager.plus(q2, q1))
# print(manager.plus(c2, c1))
# print(manager.to_glass(q1))
# print(manager.to_liter(q1))
print(manager.division_by_number(q1, 4))
print(manager.division_by_number(c1, 1))
print(manager.division_by_number(q1, 11))
print(manager.multiplication_by_number(q1, 2))
