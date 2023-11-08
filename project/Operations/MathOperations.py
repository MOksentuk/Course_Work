class MathOperations:
    def plus(self, lhs, rhs):
        """Сложение двух значений"""
        self.checker(lhs.amount, rhs.amount)

        result = lhs.amount + rhs.amount
        if self.checker(result):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        return 'В полученном значении ' + self.returner(result)

    def minus(self, lhs, rhs):
        """Вычитание двух значений"""
        self.checker(lhs, rhs)

        result = lhs.amount - rhs.amount
        return result

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
        return 'В полученном значении ' + self.returner(result)

    def multiplication_by_number(self, lhs, const):
        """Умножение на число"""
        result = lhs.amount * const
        if self.checker(result):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        return 'В полученном значении ' + self.returner(result)

    def addition_to_max_value(self, obj):
        """Дополнение до максимального значения"""
        if self.checker(obj.amount):
            raise ValueError("Полученное значение превышает максимально допустимое значение")
        max_value = 256
        result = obj.amount - max_value
        return 'В полученном значении ' + self.returner(result)