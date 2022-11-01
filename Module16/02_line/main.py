class_1 = list(range(160, 176, 2))
class_2 = list(range(162, 180, 3))

all_classes = []
all_classes.extend(class_1)
all_classes.extend(class_2)

for minimum in range(len(all_classes)):
    for number in range(minimum, len(all_classes)):
        if all_classes[number] < all_classes[minimum]:
            all_classes[number], all_classes[minimum] = all_classes[minimum], all_classes[number]

print('Отсортированный список учеников:', all_classes)
