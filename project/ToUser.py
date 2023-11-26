from Models.Quart import Quart
from Models.Gallon import Gallon
from Models.Bushel import Bushel
from Models.Storage import Storage


def to_user(manager, math, converter):
    global ans

    number_of_operation = manager.number_of_operation()
    print('Введите значения члена операции в квартах, галлонах и бушелях (для того, чтобы пропустить значение, '
          'нажмите Enter):')
    bushel = manager.init('Бушели')
    gallon = manager.init('Галлоны')
    quart = manager.init('Кварты')
    term = Storage(Quart(quart), Gallon(gallon), Bushel(bushel))
    if number_of_operation in '123':
        print('Введите значения второго члена операции в квартах, галлонах и бушелях (для того, чтобы пропустить '
              'значение, нажмите Enter):')
        bushel1 = manager.init('Бушели')
        gallon1 = manager.init('Галлоны')
        quart1 = manager.init('Кварты')
        term1 = Storage(Quart(quart1), Gallon(gallon1), Bushel(bushel1))
        if number_of_operation == '1':
            math.plus(term, term1)
            ans = manager.inverter(math.result)
        elif number_of_operation == '2':
            math.minus(term, term1)
            ans = manager.inverter(math.result)
        else:
            ans = manager.comparison_processing(math.comparison(term, term1))

    elif number_of_operation in '45':
        const = manager.init('Константа')
        if number_of_operation == '4':
            math.division_by_number(term, const)
            ans = manager.inverter(math.result)
        else:
            math.multiplication_by_number(term, const)
            ans = manager.inverter(math.result)

    elif number_of_operation == '6':
        ans = manager.addition_to_max_value_processing(math.addition_to_max_value(term))
    elif number_of_operation == '7':
        converter.to_liter(term)
        ans = manager.decorator(converter.result, 'литра', 'литр', 'литров')
    elif number_of_operation == '8':
        converter.to_glass(term)
        ans = manager.decorator(converter.result, 'стакана', 'стакан', 'стаканов')
    elif number_of_operation == '9':
        converter.to_pint(term)
        ans = manager.decorator(converter.result, 'пинты', 'пинта', 'пинт')

    return 'Ответ: ' + ans


from Manager import Manager
from Operations.Converter import Converter
from Operations.Math import MathOperations

manager = Manager()
math = MathOperations()
converter = Converter()
print(to_user(manager, math, converter))
