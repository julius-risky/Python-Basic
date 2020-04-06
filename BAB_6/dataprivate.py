class Titik(object):
    def __init__(self,x=None,y=None):
        self.__x = x
        self.__y = y
    
    def sety(self,y):
        self.__y = y
    
    def setx(self,x):
        self.__x = x
    
    def gety(self):
        return self.__y
    def getx(self):
        return self.__x

