from Models.Quart import Quart
from Models.Gallon import Gallon
from Models.Bushel import Bushel
from Manager import Manager


def main():
    q1 = Quart(11)
    g1 = Gallon(2)
    q2 = Quart(16)
    c1 = Bushel(20)
    c2 = Bushel(3)
    c3 = Bushel(1)

    manager = Manager()
    print(manager.plus(q2, q1))
    print(manager.minus(c2, c1))
    print(manager.comparison(c2, c1))
    print(manager.addition_to_max_value(c2))
    print(manager.to_glass(q1))
    print(manager.to_liter(q1))
    print(manager.division_by_number(q1, 4))
    print(manager.multiplication_by_number(c1, 4))
    print(manager.multiplication_by_number(q1, 0))
    # print(manager.multiplication_by_number(manager.summator(q1, g1, c2), 2)


if __name__ == "__main__":
    main()
