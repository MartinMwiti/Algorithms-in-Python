'''
inheritance: prevents copy and pasting codes
'''

#PART/EXAMPLE 1

class dog(object):

    def __init__(self, name, age):  # constructor method
        self.name = name  # attribute is anything having self
        self.age = age

    def speak(self):
        print('Hi, I am', self.name, 'am i am', self.age, 'yrs old')

    def talk (self):
        print('Bark!')

'''
parent/super class = dog class
child = cat class
'''

class cat(dog): #inherited all the properties, attributes and methods of the parent class

    def __init__ (self,name, age, color): #initialization of cat with added parameter 'color'
        super().__init__(name, age) #call initialization of parent class. Adds 'self.name & self.age'
        self.color = color
        #self.name = 'tech' #overide the parents self.name

    '''
    anything we do in the child/inherited class will overide the parent class when we call the child class
    '''
    def talk(self): #overrides the parent class
        print('Meow')



tim = cat('tim', 5, 'blue')
tim.speak()
tim.talk()

jim = dog('jim', 70)
jim.talk()


#PART/EXAMPLE 2

class vehicle():

    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def filluptank(self):
        self.gas = 100

    def emptytank(self):
        self.gas =0
    
    def gasleft(self):

        return self.gas

class car(vehicle):
    def __init__(self, price, gas, color, speed):
        super(). __init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print('Beep beep')


class truck(car): #can inherit properties from either parent or another child class
    def __init__(self, price, gas, color, tires):
        super(). __init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print('Honk honk')
