def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        reverse_list.append((num_list[i_num]))
    if num_list == reverse_list:
        return True
    else:
        return False


amount = int(input('Кол-во чисел: '))
numbers_list = []

for _ in range(amount):
    number = int(input('Число: '))
    numbers_list.append(number)

new_nums = []
answer = []

for i_nums in range(len(numbers_list)):
    for j_elem in range(i_nums, len(numbers_list)):
        new_nums.append(numbers_list[j_elem])

    if is_palindrome(new_nums):
        for i_answer in range(i_nums):
            answer.append(numbers_list[i_answer])
        answer.reverse()
        break
    new_nums = []

print('Последовательность:', numbers_list)
print('Нужно приписать чисел:', len(answer))
print('Сами числа:', answer)
