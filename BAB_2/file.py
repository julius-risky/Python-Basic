def main():
    #mengakses file
    f = open("F:\\python-buku_budi_raharjo\\BAB_2\\sample.txt") #mengembalikan objek
    line = f.readline() #membaca baris pertama
    while line:
        print(line, end='')
        line = f.readline() #membaca baris berikutnya
    
    #menutup file
    f.close()

if __name__ == "__main__":
    main()

import os

os.chdir("F:\\python-buku_budi_raharjo\\BAB_2\\sample.txt"):
print(line, end="")