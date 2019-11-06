import math
class Triangle(object):
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def __str__(self):
        return 'Hello' 
class Isoseles(Triangle):
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def perimiter(self):
        p=math.sqrt(((self.w/2.0)**2)+(self.h**2))
        return p
    def __str__(self):
        return f'Isoseles perimiter is {self.perimiter()}'
class equilateral(Isoseles):
    def __init__(self,w):
        self.w = w
        self.h = w
    def perimiter(self):
        p=3*self.w
        return p
    def __str__(self):
        return f'equilateral perimiter is {self.perimiter()}'