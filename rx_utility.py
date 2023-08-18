def add(x, y, *numbers):
    '''This function returns addition of x and y.'''
    sum = x + y
    for i in numbers:
        sum += i
    return sum