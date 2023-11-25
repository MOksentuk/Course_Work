class MathOperations:
    def __init__(self):
        self.result = None

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

    def multiplication_by_number(self, obj, const):
        """Деление на число"""
        self.result = obj.amount * const

    @staticmethod
    def addition_to_max_value(obj):  # Доделать
        """Дополнение до максимального значения"""
        max_value = 256
        if obj.amount > max_value:
            return False
        result = max_value - obj.amount
        return result
