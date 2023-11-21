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
    def comparison(lhs, rhs): # есть проблема с окончаниями
        """Сравнение двух значений"""
        result = abs(lhs.amount - rhs.amount)
        if lhs.amount > rhs.amount:
            return new ResultType(True, result)
        elif lhs.amount < rhs.amount:
            return False, result
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
