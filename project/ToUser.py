from Models.Quart import Quart
from Models.Gallon import Gallon
from Models.Bushel import Bushel
from Models.Storage import Storage
from Manager import Manager
from Operations.Converter import Converter
from Operations.Math import MathOperations


class ToUser:
    def __init__(self, manager):
        _manager = manager;

    
    def init(self, name):
        amount = input(f'{name}: ')

        self._manager.check_is_digit(amount)
        self._manager.check_max_value(amount)

        return amount

    
    def comparison_processing(self, res_type):
        # label = ans[0]
        # amount = ans[1]
        if res_type.status:
            return f'Первое значение больше второго на {self._manager.returner(res_type.result)}'
        elif not label:
            return f'Первое значение меньше второго на {self._manager.returner(amount)}'
        else:
            return 'Значения равны'
