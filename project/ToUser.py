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
        f = f'Значение в : '
        print(f)
        amount = input()
        # gallon = input('Значение в галлонах: ')
        # bushel = input('Значение в бушелях: ')

        self.manager.checker(amount)
        return amount
        # self.manager.checker(gallon)
        # self.manager.checker(bushel)

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
ToUser.init('o')
