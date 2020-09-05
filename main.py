def count():
    numbers = [1,2,3]
    for number in numbers:
        print(number)

def sum():
    s = 0
    numbers = [1,2]
    for number in numbers:
        s = s + number
    return s

def product():
    s = 1
    numbers = [1,2,3,4]
    for number in numbers:
        s = s * number
    return s

p = product()

print(p)
