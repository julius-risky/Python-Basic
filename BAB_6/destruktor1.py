#mendefinisikan kelas
class myfile(object):
    def __init__(self, namafile):
        self.file = open(namafile)
    def __del__(self):
        self.file.close()
    def bacadata(self):
        for baris in self.file:
            print(baris,end='')


if __name__ == "__main__":
    main()