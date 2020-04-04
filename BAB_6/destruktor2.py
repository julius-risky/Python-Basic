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

def main():
    #membuat object dari kelas myfile
    f = myfile("F:\\python-buku_budi_raharjo\\BAB_6\\sample.txt")
    
    #memanggil baca data
    f.bacadata()

if __name__ == "__main__":
    main()