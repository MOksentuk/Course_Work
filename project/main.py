from Models.Quart import Quart
from Models.Gallon import Gallon
from Models.Bushel import Bushel
from Models.Storage import Storage
from Manager import Manager


def main():
    q1 = Quart(11)
    g1 = Gallon(2)
    q2 = Quart(16)
    b1 = Bushel(20)
    b2 = Bushel(3)
    b3 = Bushel(1)
    # 1 2 3 (+-/*) 1 2 3
    manager = Manager()
    storage = Storage(b1, 0, q1)
    manager.plus(q1, b1)


if __name__ == "__main__":
    main()
