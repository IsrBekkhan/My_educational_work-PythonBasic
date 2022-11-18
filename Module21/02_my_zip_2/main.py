def my_zip(*args):
    minimum = min(list((len(elem) for elem in args)))
    return [
        tuple(list(i_element)[index] for i_element in args)
           for index in range(minimum)
           ]


a = [1, 2, 3, 4, 5]
b = {1: "s", 2: "q", 3: 4}
x = (1, 2, 3, 4, 5)

print(my_zip(a, b, x))
