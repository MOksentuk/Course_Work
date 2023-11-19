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
    to_user = ToUser()
    math = MathOperations()
    converter = Converter()
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
    if number_of_operation not in '123456789':
        raise ValueError('Переданное значение не является номером операции')
    print('!Введите значения члена операции в квартах, галлонах и бушелях (для того, чтобы пропустить значение, '
          'нажмите Enter)!')
    bushel = to_user.init('Бушели')
    gallon = to_user.init('Галлоны')
    quart = to_user.init('Кварты')
    term = Storage(Quart(quart), Gallon(gallon), Bushel(bushel))
    if number_of_operation in '123':
        print('!Введите значения второго члена операции в квартах, галлонах и бушелях (для того, чтобы пропустить '
              'значение, нажмите Enter)!')
        bushel1 = to_user.init('Бушели')
        gallon1 = to_user.init('Галлоны')
        quart1 = to_user.init('Кварты')
        term1 = Storage(Quart(quart1), Gallon(gallon1), Bushel(bushel1))
        if number_of_operation == '1':
            ans = manager.inverter(math.plus(term, term1))
        if number_of_operation == '2':
            ans = manager.inverter(math.minus(term, term1))
        if number_of_operation == '3':
            ans = to_user.comparison_processing(math.comparison(term, term1))

    elif number_of_operation in '45':
        const = to_user.init('Константа')
        if number_of_operation == '4':
            ans = manager.inverter(math.division_by_number(term, const))
        if number_of_operation == '5':
            ans = manager.inverter(math.multiplication_by_number(term, const))

    elif number_of_operation == '6':
        ans = math.addition_to_max_value(term)
    elif number_of_operation == '7':
        ans = manager.decorator(converter.to_liter(term), 'литра', 'литр', 'литров')
    elif number_of_operation == '8':
        ans = manager.decorator(converter.to_glass(term), 'стакана', 'стакан', 'стаканов')
    elif number_of_operation == '9':
        ans = manager.decorator(converter.to_pint(term), 'пинты', 'пинта', 'пинт')

    print(ans)


if __name__ == "__main__":
    main()
