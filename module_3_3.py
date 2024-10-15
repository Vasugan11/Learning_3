def print_params(a=1, b="string", c=True):
    print(a,b,c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])


def print_params(a=1, b="string", c=True, d=3, e="st", f=4):
    print(a, b, c, d, e, f)

values_list = [2, '1', False]
values_dict = {'d': 5, 'e': '7', 'f': 5.6}

print_params(*values_list, **values_dict)


def print_params(a, b, c):
    print(a, b, c)

values_list_2 = [5, '7']

print_params(*values_list_2, 42)