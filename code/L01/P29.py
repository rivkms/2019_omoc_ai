import math  # for math.pi

class Point:
    # modifier
    def __init__(self, px, py):
        self.x = px
        self.y = py

    # pure function
    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ")"
        
    # pure function
    def getX(self):
        return self.x
    
    # pure function
    def getY(self) :
        return self.y
    
    # modifier
    def setX(self, v):
        self.x = v
        
    # modifier
    def setY(self, v):
        self.y = v
        
    # pure function
    def distance(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return (dx*dx + dy*dy)**0.5
    
    # pure function
    def add(self, p):
        x = self.x + p.x
        y = self.y + p.y
        return Point(x,y)

    # modifier version of the add function
    def add_as_modifier(self, p):
        self.x += p.x
        self.y += p.y
        
########################################

class Circle:
    # modifier
    def __init__(self, c, r):
        pass # remove it after completing your code
        # ADD ADDITIONAL CODE HERE!

    # pure function
    def __str__(self):
        pass # remove it after completing your code
        # ADD ADDITIONAL CODE HERE!

    # pure function
    def area(self):
        pass # remove it after completing your code
        # ADD ADDITIONAL CODE HERE!
        
    # pure function
    def getRadius(self):
        pass # remove it after completing your code
        # ADD ADDITIONAL CODE HERE!

    # pure function
    def getCenter(self):
        pass # remove it after completing your code
        # ADD ADDITIONAL CODE HERE!

    # modifier
    def setRadius(self, v):
        pass # remove it after completing your code
        # ADD ADDITIONAL CODE HERE!

    # modifier
    def moveTo(self, x, y):  
        pass # remove it after completing your code
        # ADD ADDITIONAL CODE HERE!

    # modifier
    def move(self, dx, dy):
        pass # remove it after completing your code
        # ADD ADDITIONAL CODE HERE!

    
def test():
    p0 = Point (0,0)       
    c1 = Circle(p0,3)
    print(c1)                # ((0,0) , 3)
    print(c1.area())         # 28.274333882308138
    print(c1.getRadius())    # 3
    print(c1.getCenter())    # (0,0)
    
    c1.setRadius(5)
    print(c1)                # ((0,0) , 5)
    print(c1.area())         # 78.53981633974483
    
    c1.moveTo(3,4)          
    print(c1)                # ((3,4) , 5)
    
    c1.move(1,1)
    print(c1)                # ((4,5) , 5)

if __name__ == '__main__': test()
