def histogram(text):
    text_dictonary = dict()

    for letter in text:
        if letter in text_dictonary:
            text_dictonary[letter] += 1
        else:
            text_dictonary[letter] = 1
    return text_dictonary


def hist_inverse(dictonary):
    new_dictonary = dict()

    for key in dictonary:
        value = dictonary[key]

        if value not in new_dictonary:
            new_dictonary[value] = [key]
        else:
            new_dictonary[value].append(key)

    return new_dictonary


text = input('Ведите текст: ')
hist_dictonary = histogram(text)

print('\nОригинальный словарь частот:')
for key in hist_dictonary:
    print(key, ':', hist_dictonary[key])

inverted_hist = hist_inverse(hist_dictonary)
print('\nИнвертированный словарь частот:')
for elem in inverted_hist:
    print(elem, ':', inverted_hist[elem])