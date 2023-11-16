# class Course(object):
#     """Mediator class."""
#
#     def displayCourse(self, user, course_name):
#         print("[{}'s course ]: {}".format(user, course_name))
#
#
# class User(object):
#     """A class whose instances want to interact with each other."""
#
#     def __init__(self, name):
#         self.name = name
#         self.course = Course()
#
#     def sendCourse(self, course_name):
#         self.course.displayCourse(self, course_name)
#
#     def __str__(self):
#         return self.name
#
#
# """main method"""
#
# if __name__ == "__main__":
#     mayank = User('Mayank')  # user object
#     lakshya = User('Lakshya')  # user object
#     krishna = User('Krishna')  # user object
#
#     mayank.sendCourse("Data Structures and Algorithms")
#     lakshya.sendCourse("Software Development Engineer")
#     krishna.sendCourse("Standard Template Library")
print(str(abs(-3)).isdigit())


from Models.Quart import Quart
from Models.Gallon import Gallon
from Models.Bushel import Bushel
from Models.Storage import Storage
from Manager import Manager
from Operations.Converter import Converter
from Operations.Math import MathOperations
# from ToUser import ToUser
manager=Manager()
q1 = Quart(1)
q2 = Quart(2)
g1 = Gallon(1)
g2 = Gallon(2)
b1 = Bushel(1)
b2 = Bushel(2)
b3 = Bushel(3)
const1 = 1
const2 = 2
const3 = 555
# 1 2 3 (+-/*) 1 2 3
obj1 = Storage(quart=q1.amount, gallon=g1.amount, bushel=b1.amount)
obj2 = Storage(quart=q2.amount, gallon=g2.amount, bushel=b2.amount)
# print(Converter().to_liter(manager, q1))
print(manager.returner(MathOperations().minus(obj1, obj2)))
# print(manager.returner(MathOperations().multiplication_by_number(obj1, const3)))
