from Models.Quart import Quart
from Models.Gallon import Gallon
from Models.Bushel import Bushel
from Models.Storage import Storage
from Manager import Manager
from Operations.Converter import Converter
from Operations.Math import MathOperations


class ToUser:

    def __setattr__(self, key, value):
        self.amount = None
        # if amount != '':
        #     self.amount += int(amount)

    obj1 = Storage([])

# a=input()
# b=input()
# if a!='':
#     print(a)
# else:
#     print('Nothing')
