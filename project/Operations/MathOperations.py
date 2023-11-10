class MathOperations:
    @staticmethod
    def plus(lhs, rhs):
        """Сложение двух значений"""

        result = lhs + rhs
        return result

    @staticmethod
    def minus(lhs, rhs):
        """Вычитание двух значений"""

        result = lhs - rhs
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
    def division_by_number(amount, const):
        """Деление на число"""
        result = amount / const
        return result

    @staticmethod
    def multiplication_by_number(amount, const):
        """Умножение на число"""
        result = amount * const
        return result

    @staticmethod
    def addition_to_max_value(amount):
        """Дополнение до максимального значения"""
        max_value = 256
        result = amount - max_value
        return result
