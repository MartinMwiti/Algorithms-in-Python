'''f strings: alternative from using '%s' or '+value' or .format()  and it's faster'''
name = 'martin'
age = 20

ex1 = F'my name is {name} and i am {age+5} years old' #you can use any case for 'f'
print(ex1)


'''swapping variable'''
a = 65
b = 45

a , b = b , a
print(a, b)

'''list comprehension'''
x = [i for i in range(10) if i%2==0]

print(x)

#two loops
y = [(i, y) for i in range(10) for y in range(20)]

print(y)

Z = [0 for i in range(10)]

print(Z)


'''Tuple Decomposition: getting specific elements'''
t1 = (1,2)
t2 = (1,2,3)

x, y = t1
print(x,y)

'''zip function: matches items in a list'''
x = [1,2,3,4]
y = [1,1,3,7,9]

print(list(zip(x,y)))

for i, j in zip(x,y):
    if i==j:
        print ('Same')
    else:
        print('Not Same')


'''for else statement'''
my_list = [100,55,67,89,99,101,23,44,100,23]
look_for = 45
#checks all values first then if it's not found, prints 'Did not find'
for x in my_list:
    if x == look_for:
        print('Found', look_for)
        break
else:
    print('Did not find', look_for)

#checks one values at a time then if it's not found in each loop, prints 'Did not find'
for x in my_list:
    if x == look_for:
        print('Found', look_for)
        break
    else:
        print('Did not find', look_for)


'''enumerate function: loop not only index but also element as well'''
my_list = ['apples', 'pears', 'oranges', 'fruits']

for x, element in enumerate(my_list): #x is the index, element is the object name
    print(x, element)

for x, element in enumerate(my_list):
    #print(x, element)
    if x==1:
        print(f'element of interest is {element}')
