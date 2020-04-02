#mendefinisikan kelas
class kotak(object):
    def __init__(self,p=0,l=0,t=0):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
    def setdata(self,p,l,t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
    def hitungvolume(self):
        return self.panjang * self.lebar *self.tinggi
    def cetakData(self):
        print("Panjang\t: ",self.panjang)
        print("lebar\t: ",self.lebar)
        print("tinggi\t: ",self.tinggi)
    def cetakVolume(self):
        print("Volume\t: ",self.hitungvolume())

def main():
    kotak1 = kotak() 
    kotak1.setdata(8,4,2)
    print("object pertama")
    kotak1.cetakData()
    kotak1.cetakVolume()

if __name__ == "__main__":
    main()