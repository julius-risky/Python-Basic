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

class kotakwarna(kotak):
    def __init__(self,p,l,t,w):
        #memanggil kotak.__init__
        #super(kotakwarna,self).__init__(p,l,t)
        super().__init__(p,l,t)
        #menambah atribut baru
        self.warna = w
    
    def cetakData(self):
        #memanggi kotak.cetakdata
        #super(kotakwarna,self).cetakData()
        super().cetakData()
        print("warna\t: ",self.warna)

def main():
    print("object ke-1")
    kotakwarna1 = kotakwarna(6,5,4,"pink")
    kotakwarna1.cetakData()
    kotakwarna1.cetakVolume()

if __name__ == "__main__":
    main()