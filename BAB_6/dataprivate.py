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

def main():
    #membuat object titik
    A = Titik()

    #memasukkan nilai __x dan __y dalam A
    A.setx(4)
    A.sety(5)

    #mengambil nilai __x dan __y di dalam A
    print("A(%d, %d)"%(A.getx(),A.gety()))

if __name__ == "__main__":
    main()
