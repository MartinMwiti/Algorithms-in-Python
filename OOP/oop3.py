'''
overloading method
'''
class point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
         self.x += x
         self.y += y

    def __add__(self, p):
        return point(self.x + p.x, self.y + p.y)



p1 = point(3,4)
p2 = point(3,2)
p3 = point(1,3)
p4 = point(0,1)
p1 + p2