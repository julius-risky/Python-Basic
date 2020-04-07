class titik(object):
    def __init__(self,x=None,y=None):
        self.__x = x
        self.__y = y 

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,Nilai):
        if (not isinstance(Nilai,int)) and (not isinstance(Nilai,float)):
            raise TypeError("x harus bertipe numerik")
        self.__x = Nilai
    
    @x.deleter
    def x(self):
        del self.__x #menghapus self.__x dari memori

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,Nilai):
        if (not isinstance(Nilai,int)) and (not isinstance(Nilai,float)):
            raise TypeError("y harus bertipe numerik")
        self.__y = Nilai
    
    @y.deleter
    def y(self):
        del self.__y #menghapus self.__y dari memori

def main():
    #memubuat object dari kelas titik
    A = titik()
    B = titik(5,6)

    #menentukan nilai __x dan __y di dalam A
    #melalui properti x dan y
    A.x = 10
    A.y = 20

    #mengambil nilai__x dan __y di A melalui prperti
    print("A(%d, %d)"%(A.x,A.y))

    print("B(%d, %d)"%(B.x,B.y))
if __name__ == "__main__":
    main()