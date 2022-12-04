input_data = open('zen.txt', 'r')
text_list = input_data.read().split('\n')
print('\n'.join(reversed(text_list)))
input_data.close()
