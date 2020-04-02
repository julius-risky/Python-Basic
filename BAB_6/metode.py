#mendefinisikan kelas
class kotak(object):
    def __init__(self,p,l,t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
    def hitungvolume(self):
        return self.panjang * self.lebar *self.tinggi
    def cetakData(self):
        print("\nobject" + self)
        print("Panjang\t: ",self.panjang)
        print("lebar\t: ",self.lebar)
        print("tinggi\t: ",self.tinggi)
    def cetakVolume(self):
        print("Volume\t: ",self.hitungvolume())

def main():
    kotak1 = kotak(8,4,2)
    kotak1.cetakData()
    kotak1.cetakVolume()

    kotak2 = kotak(12,9,7)
    kotak2.cetakData()
    kotak2.cetakVolume()
if __name__ == "__main__":
    main()
