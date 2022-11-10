def histogram(text):
    text_dictonary = dict()

    for letter in text:
        if letter in text_dictonary:
            text_dictonary[letter] += 1
        else:
            text_dictonary[letter] = 1
    return text_dictonary

def hist_inverse(dictonary):
    keys_set = set(dictonary.values())
    new_dictonary = dict()

    for value in keys_set:
        new_dictonary[value] = []

    for i_key in new_dictonary:
        for j_key in dictonary:
            if dictonary[j_key] == i_key:
                new_dictonary[i_key].append(j_key)

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