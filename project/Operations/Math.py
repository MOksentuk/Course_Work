class MathOperations:
    @staticmethod
    def plus(lhs, rhs):
        """Сложение двух значений"""

        result = lhs.amount + rhs.amount
        return result

    @staticmethod
    def minus(lhs, rhs):
        """Вычитание двух значений"""

        result = lhs.amount - rhs.amount
        return result

    @staticmethod
    def comparison(lhs, rhs):
        """Сравнение двух значений"""
        result = abs(lhs.amount - rhs.amount)
        if lhs.amount > rhs.amount:
            return 1, result
        elif lhs.amount < rhs.amount:
            return -1, result
        else:
            return 0

    @staticmethod
    def division_by_number(obj, const):
        """Деление на число"""
        result = obj.amount / const
        return result

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
