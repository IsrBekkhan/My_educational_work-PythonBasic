def calculater(task):
    elements_list = task.split()
    try:
        if len(elements_list) < 3:
            raise IndexError('Введены не все элементы операции.')
        elif len(elements_list) > 3:
            raise IndexError('Превышено количество элементов в операции')
        else:
            operand_1, operation, operand_2 = int(elements_list[0]), elements_list[1], int(elements_list[2])
            operation_dict = {'+': operand_1 + operand_2,
                              '-': operand_1 - operand_2,
                              '*': operand_1 * operand_2,
                              '/': operand_1 / operand_2,
                              '//': operand_1 // operand_2,
                              '%': operand_1 % operand_2}

            if not operation in operation_dict:
                raise SyntaxError('Введено неверное обозначение знака операции')
            else:
                result = operation_dict[operation]

    except (IndexError, ValueError, SyntaxError) as exc:
        return False
    except TypeError('Введеное значение не является числом'):
        return False
    except ZeroDivisionError('Деление на ноль не допускается.'):
        return False
    else:
        return result


def fix_operation(operation):
    choice = input('Обнаружена ошибка в строке: {task}   Хотите исправить? '.format(
        task=operation)).lower()
    while not choice in ('да', 'нет'):
        choice = input('Ошибка ввода. Повторите попытку: ').lower()

    if choice == 'да':
        new_operation = input('Введите исправленную строку: ')
        result = calculater(new_operation)
        if result:
            return result
        else:
            new_result = fix_operation(new_operation)
            return new_result
    else:
        return 0


total_sum = 0

with open('calc.txt', 'r', encoding='utf-8') as task_list:
    for task in task_list:
        result = calculater(task)

        if result:
            total_sum += result
        else:
            try:
                total_sum += fix_operation(task)
            except RecursionError:
                print('Слишком много неверных вводов')

print('Сумма результатов:', round(total_sum, 2))


