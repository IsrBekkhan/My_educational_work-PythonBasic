def simple_iteration(collection):
    return [value for index, value in enumerate(collection) if is_prime(index)]

def is_prime(number):
    if number == 0 or number == 1:
        return False
    for digit in range(2, number):
        if number % digit == 0:
            return False
    return True

print(simple_iteration([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))