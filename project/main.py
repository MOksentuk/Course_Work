from Models.Quart import Quart
from Models.Gallon import Gallon
from Models.Bushel import Bushel
from Models.Storage import Storage
from Manager import Manager
from Operations.Converter import Converter
from Operations.Math import MathOperations


def main():
    q1 = Quart(1)
    q2 = Quart(2)
    g1 = Gallon(1)
    g2 = Gallon(2)
    b1 = Bushel(1)
    b2 = Bushel(2)
    b3 = Bushel(3)
    const1 = 0
    const2 = 2
    const3 = 555
    # 1 2 3 (+-/*) 1 2 3
    manager = Manager()
    obj1 = Storage(quart=q1.amount, gallon=g1.amount, bushel=b1.amount)
    obj2 = Storage(quart=q2.amount, gallon=g2.amount, bushel=b2.amount)
    # print(Converter().to_liter(manager, q1))
    print(manager.returner(MathOperations().plus(obj1, obj2)))
    print(manager.returner(MathOperations().multiplication_by_number(obj1, const3)))


if __name__ == "__main__":
    main()
