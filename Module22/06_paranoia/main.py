def cezar_decrypt(user_string, shift):
    alphabet_low = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted_letters = []

    for symbol in user_string:
        if symbol.islower():
            decrypted_letters.append(alphabet_low[(alphabet_low.index(symbol) + shift) % 26])
        elif symbol.isupper():
            decrypted_letters.append(alphabet_up[(alphabet_up.index(symbol) + shift) % 26])
        else:
            decrypted_letters.append(symbol)

    return ''.join(decrypted_letters)


input_data = open('text.txt', 'r', encoding='utf-8')
step = 1

for string in input_data:
    encrypted_string = cezar_decrypt(string, step)
    output_data = open('cipher_text.txt', 'a', encoding='utf-8')
    output_data.write(encrypted_string)
    output_data.close()
    step += 1