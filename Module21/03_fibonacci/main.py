fibonachi_list = [1, 1]
def fibonachi_series(num):
    if len(fibonachi_list) >= num:
        return
    prev_sum = fibonachi_list[-1] + fibonachi_list[-2]
    fibonachi_list.append(prev_sum)
    fibonachi_series(num)

num = int(input('Введите позицию числа в ряде Фибоначчи: '))
fibonachi_series(num)
print('Число:', fibonachi_list[num - 1])
