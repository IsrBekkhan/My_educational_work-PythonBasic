input_data = open('numbers.txt', 'r')
total_sum = 0

for elem in input_data:
    number = elem.split()
    if len(number) > 0:
        total_sum += int(number[0])

input_data.close()

output_data = open('answer.txt', 'w')
output_data.write(str(total_sum))
output_data.close()

