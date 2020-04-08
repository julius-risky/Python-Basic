#membuat kelas induk (superclass)
class kotak(object):
    def __init__(self,p,l,t):
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
#mendefinisikan turunan (subclass)
class kotakwarna(kotak):
    def __init__(self,p,l,t,w):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
        self.warna = w
    def cetakData(self):
        print("Panjang\t: ",self.panjang)
        print("lebar\t: ",self.lebar)
        print("tinggi\t: ",self.tinggi)
        print("warna\t: ",self.warna)

def main():
    #membuat object kotak warna
    kotakwarna1 = kotakwarna(6,5,4,"kuning")

    #menggunakan object
    kotakwarna1.cetakData()
    kotakwarna1.hitungvolume()

if __name__ == "__main__":
    main()