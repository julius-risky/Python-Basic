#mendefinisikan kelas
class myfile(object):
    def __init__(self, namafile):
        print("membuka file %s ...\n"%namafile)
        self.file = open(namafile)
    def __del__(self):
        self.file.close()
        print("\nmenutup file")
    def bacadata(self):
        for baris in self.file:
            print(baris,end='')
