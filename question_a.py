def overlap(x1, x2, x3, x4):
    line_one, line_two = list(range(x1, x2 + 1)), list(range(x3, x4 + 1))
    if line_one[0] >= line_two[-1] or line_two[0] >= line_one[-1]:
        print('Not overlap!')
    else:
        print('Overlap!')