#mendefinisikan kelas
class kotak(object):
    def __init__(self,p,l,t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
    def hitungvolume(self):
        return self.panjang * self.lebar *self.tinggi

def main():
    kotak1 = kotak(6,5,7)
    print("object kotak1")
    print("Panjang\t: ",kotak1.panjang)
    print("lebar\t: ",kotak1.lebar)
    print("tinggi\t: ",kotak1.tinggi)
    print("Volume\t: ",kotak1.hitungvolume())

if __name__ == "__main__":
    main()