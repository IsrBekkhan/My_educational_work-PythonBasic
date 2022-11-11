def zip_function(combination_1, combination_2):
    tuple_list = (
        (combination_1[index], combination_2[index])
        for index in range(min(len(combination_1), len(combination_2)))
    )
    return tuple_list

text = 'abcd'
numbers = (10, 20, 30, 40)

result = zip_function(text, numbers)
print(result)

for value in result:
    print(value)