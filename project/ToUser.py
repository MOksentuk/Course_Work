def to_user(manager, math, converter):
    """Работа с пользователем"""
    while True:
        ans = ''
        number_of_operation = manager.number_of_operation()
        
        if not number_of_operation:
            print('Работа окончена.')
            break
            
        term1 = manager.term('первого')
        
        if number_of_operation in '123':
            term2 = manager.term('второго')
            if number_of_operation == '1':
                math.plus(term1, term2)
                ans = manager.inverter(math.result)
            elif number_of_operation == '2':
                math.minus(term1, term2)
                ans = manager.inverter(math.result)
            else:
                ans = manager.comparison_processing(math.comparison(term1, term2))

        elif number_of_operation in '45':
            const = manager.init('Введите константу')
            if number_of_operation == '4':
                math.division_by_number(term1, const)
            else:
                math.multiplication_by_number(term1, const)
            ans = manager.inverter(math.result)

        elif number_of_operation == '6':
            ans = manager.addition_to_max_value_processing(math.addition_to_max_value(term1))

        elif number_of_operation == '7':
            converter.to_liter(term1)
            ans = manager.decorator(converter.result, 'литра', 'литр', 'литров')
            
        elif number_of_operation == '8':
            converter.to_glass(term1)
            ans = manager.decorator(converter.result, 'стакана', 'стакан', 'стаканов')
            
        else:
            converter.to_pint(term1)
            ans = manager.decorator(converter.result, 'пинты', 'пинта', 'пинт')

        print('Ответ: ' + ans + '\n')
