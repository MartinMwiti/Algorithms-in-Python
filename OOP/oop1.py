'''
creating class
'''

class dog(object):

    def __init__ (self, name, age): #constructor method
        self.name = name #attribute is anything having self
        self.age = age
        self.li = [1,2,3]

    def speak(self):
        print( 'Hi, I am', self.name, 'am i am', self.age, 'yrs old')

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight #creating new attribute


fred = dog('Tim', 40) #fred is the instance 'self'
fred.speak()
fred.change_age(23)
fred.speak()

print(fred.age)
print(fred.li)

fred.add_weight(70)
print(fred.weight)
