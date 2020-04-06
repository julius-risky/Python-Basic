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

def main():

    kotak1 = kotak(8,4,2) 
    print("object pertama")
    kotak1.cetakData()
    kotak1.cetakVolume()
    print("object counter = ",kotak1.objectCunter)

    print("\n object kedua")
    kotak2 = kotak(12,9,7)
    kotak2.cetakData()
    kotak2.cetakVolume()
    print("object counter= ",kotak2.objectCunter)
    #menghapus object aau menutup

    print("\n Object ke-3")
    kotak3= kotak(19,8,7)
    kotak3.cetakData()
    kotak3.cetakVolume()
    print("object counter= ",kotak3.objectCunter)

    print("\nobject kounter pada object pertama= ",kotak1.objectCunter)
    print(" object kounter pada object kedua= ",kotak2.objectCunter)
    print(" object kounter pada object ke-3= ",kotak3.objectCunter)
if __name__ == "__main__":
    main()