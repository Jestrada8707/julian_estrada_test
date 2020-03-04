"""This function analise two parameters and print which one is even or not"""


def is_even_number(x, y):
    if x % 2 == 0:
        print ('The value {} is even'.format(x))
    else:
        print ('The value {} is not even'.format(x))
    if y % 2 == 0:
        print ('The value {} is even'.format(y))
    else:
        print ('The value {} is not even'.format(y))


"""This function only return which value is negative"""


def is_negative_value(x, y):
    if x < 0:
        print('The value {} is negative'.format(x))
    elif y < 0:
        print('The value {} is negative'.format(y))
