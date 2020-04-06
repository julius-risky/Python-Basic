class tanggal(object):
    def __init__(self,dd=0,mm=0,yy=0):
        self.hari = tanggal.hari = dd
        self.bulan = tanggal.bulan = mm
        self.tahun = tanggal.tahun= yy

    @classmethod
    def daristring(cls, strTanggal):
        hari,bulan,tahun = map(int, strTanggal.split('-'))
        objectTanggal = cls(hari,bulan,tahun)
        return objectTanggal
    
    def cetaktanggal(self):
        BULAN = ["januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
        print("%d %s %d"%(self.hari,BULAN[self.bulan-1],self.tahun))
    

def main():
    #membuat object dari kelas tanggal
    #menggunakan cara umum
    obj1 = tanggal(19,8,2020)

    #membuat object dari kelas tanggal dengan metde kelas
    obj2 = tanggal.daristring("13-7-2020")

    print("tanggal obj1: ",end='')
    obj1.cetaktanggal()
    print("tanggal obj2: ",end='')
    obj2.cetaktanggal()
if __name__ == "__main__":
    main()
    