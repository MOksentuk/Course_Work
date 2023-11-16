from Models.Quart import Quart
from Models.Gallon import Gallon
from Models.Bushel import Bushel
from Models.Storage import Storage
from Manager import Manager
from Operations.Converter import Converter
from Operations.Math import MathOperations
from ToUser import ToUser


def main():
    manager = Manager()

    number_of_operation = input('Выберите номер операции:\n'
                                '1. Сложение\n'
                                '2. Вычитание\n'
                                '3. Сравнение\n'
                                '4. Деление на число\n'
                                '5. Умножение на число\n'
                                '6. Дополнение до максимального значения\n'
                                '7. Перевод в литры\n'
                                '8. Перевод в стаканы\n'
                                '9. Перевод в пинты\n>>>')
    print('Введите значения в квартах, галлонах и бушелях (для того, чтобы пропустить значение, нажмите Enter)')
    quart = ToUser.init('квартах')
    # quart = input('Значение в квартах: ')
    # gallon = input('Значение в галлонах: ')
    # bushel = input('Значение в бушелях: ')
    # manager.checker(quart)
    # manager.checker(gallon)
    # manager.checker(bushel)

    if number_of_operation in '123':
        quart1 = input('Значение в квартах: ')
        gallon1 = input('Значение в галлонах: ')
        bushel1 = input('Значение в бушелях: ')
        manager.check_is_digit(quart1)
        manager.check_is_digit(gallon1)
        manager.check_is_digit(bushel1)

    # q1 = Quart(1)
    # q2 = Quart(2)
    # g1 = Gallon(1)
    # g2 = Gallon(2)
    # b1 = Bushel(1)
    # b2 = Bushel(2)
    # b3 = Bushel(3)
    # const1 = 1
    # const2 = 2
    # const3 = 555
    # # 1 2 3 (+-/*) 1 2 3
    # obj1 = Storage(quart=q1.amount, gallon=g1.amount, bushel=b1.amount)
    # obj2 = Storage(quart=q2.amount, gallon=g2.amount, bushel=b2.amount)
    # print(Converter().to_liter(manager, q1))
    # print(manager.returner(MathOperations().plus(obj1, obj2)))
    # print(manager.returner(MathOperations().multiplication_by_number(obj1, const3)))


if __name__ == "__main__":
    main()
