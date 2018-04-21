import math

class Line(object):

    def __init__(self,x = 0, y = 0, x1 = 0, y1 = 0):
        self.x = x
        self.x1 = x1
        self.y = y
        self.y1 = y1

    def __repr__(self):
        self.point1 = (self.x, self.y)
        self.point2 = (self.x1, self.y1)
        return repr((self.point1, self.point2))

    def __length__(self):
        return math.sqrt((self.x - self.x1) * (self.x - self.x1) + (self.y - self.y1) * (self.y - self.y1))


    def __slope__(self):
        return ((self.x - self.x1) / (self.y - self.y1))


k = Line(1,1,2,2)
print k.__slope__()