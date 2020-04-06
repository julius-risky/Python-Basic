#mendefinisikan kelas
class kotak(object):
    objectCunter = 0 
    def __init__(self,p,l,t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
        kotak.objectCunter +=1
    def hitungvolume(self):
        return self.panjang * self.lebar *self.tinggi
    def cetakData(self):
        print("Panjang\t: ",self.panjang)
        print("lebar\t: ",self.lebar)
        print("tinggi\t: ",self.tinggi)
    def cetakVolume(self):
        print("Volume\t: ",self.hitungvolume())
    @staticmethod
    def cetakJudul():
        if kotak.objectCunter >=1:
            print() #baris baru
            print("KOTAK KE-",kotak.objectCunter)

def main():

    kotak1 = kotak(8,4,2) 
    kotak.cetakJudul()
    kotak1.cetakData()
    kotak1.cetakVolume()

    kotak2 = kotak(12,9,7)
    kotak.cetakJudul()
    kotak2.cetakData()
    kotak2.cetakVolume()

    kotak3= kotak(19,8,7)
    kotak.cetakJudul()
    kotak3.cetakData()
    kotak3.cetakVolume()

if __name__ == "__main__":
    main()