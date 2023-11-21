from Models.Quart import Quart
from Models.Gallon import Gallon
from Models.Bushel import Bushel
from Models.Storage import Storage
from Manager import Manager
from Operations.Converter import Converter
from Operations.Math import MathOperations


class ToUser:
    manager = Manager()
  
    def init(self, name):
        amount = input(f'{name}: ')

        self.manager.check_is_digit(amount)
        self.manager.check_max_value(amount)

        return amount

    def comparison_processing(self, ans):
        label = ans[0]
        amount = ans[1]
        if label:
            return f'Первое значение больше второго на {self.manager.returner(amount)}'
        elif not label:
            return f'Первое значение меньше второго на {self.manager.returner(amount)}'
        else:
            return 'Значения равны'
