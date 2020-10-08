""" this is my first module & script """

def my_func1(x):
    return print(x**2)

def my_func2(y):
    return print(*y)

from ..asia import japan  # we've added importing syntax using two dots
japan.my_func1(6)         # and the name of parent subpackage (asia)

if __name__ == '__main__':
    print('hello') 
    my_func1(3)
    my_func2("clarusway")
