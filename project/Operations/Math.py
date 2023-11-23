class MathOperations:
    result = ''

    def plus(self, lhs, rhs):
        """Сложение двух значений"""

        self.result = lhs.amount + rhs.amount

    def minus(self, lhs, rhs):
        """Вычитание двух значений"""

        self.result = lhs.amount - rhs.amount

    @staticmethod
    def comparison(lhs, rhs):  # есть проблема с окончаниями
        """Сравнение двух значений"""
        result = abs(lhs.amount - rhs.amount)
        if lhs.amount > rhs.amount:
            return True, result
        elif lhs.amount < rhs.amount:
            return False, result
        else:
            return None, 0

    def division_by_number(self, obj, const):
        """Деление на число"""
        self.result = obj.amount / const

    @staticmethod
    def multiplication_by_number(obj, const):
        """Умножение на число"""
        result = obj.amount * const
        return result

    @staticmethod
    def addition_to_max_value(obj):
        """Дополнение до максимального значения"""
        max_value = 256
        result = obj.amount - max_value
        return result
