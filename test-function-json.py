def my_func(args):
    for arg in args:
        print(arg)

my_func({'name': 'amir', 'family': 'shakery', 'age': '19'})

def second_func(**kwargs):
    for i in kwargs.keys():
        print(kwargs.values())

# ** for dictionaries and * for variables
