from Models.Quart import Quart
from Models.Gallon import Gallon
from Models.Bushel import Bushel
from Models.Storage import Storage
from Manager import Manager
from Operations.Converter import Converter
from Operations.Math import MathOperations

manager = Manager()


class ToUser:

    def init(self, name):
        f = f'Значение в {name}: '
        print(f)
        amount = 6
        # gallon = input('Значение в галлонах: ')
        # bushel = input('Значение в бушелях: ')

        manager.check_is_digit(amount)
        return amount

    # def __setattr__(self, key, value):
    #     self.amount = None
    # if amount != '':
    #     self.amount += int(amount)

    # obj1 = Storage([])


# a=input()
# b=input()
# if a!='':
#     print(a)
# else:
#     print('Nothing')
a = 'o'
ToUser().init(name='квартах')
