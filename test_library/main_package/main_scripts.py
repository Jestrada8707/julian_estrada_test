"""This function compare two parameters and print which one is greater"""

def greater_than(x, y):
    if x > y:
        print('The value {} is greater than {}'.format(x, y))
    elif y > x:
        print('The value {} is greater than {}'.format(y, x))
    else:
        print('The values are equal!')
