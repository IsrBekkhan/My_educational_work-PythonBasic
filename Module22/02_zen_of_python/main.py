input_data = open('zen.txt', 'r')
text_list = input_data.read().split('\n')
text_list.reverse()
print('\n'.join(text_list))

