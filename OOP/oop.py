x = 5
y = 'string'

print(type(x))
print(type(y))

print(y.upper()) #.upper is not a func but a method that apply to the class str

'''
1. method is anything you're calling on an object itself.
2. function is sth that takes an object and apply an operation to it.
'''

def func(x):
    return x + 1

print(func(3))