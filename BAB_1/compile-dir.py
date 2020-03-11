import os, compileall

def main():
    dir = "F:\\python-buku_budi_raharjo\\BAB_1"
    compileall.compile_dir(dir)
    #print("semua file dalam %d telah di ompilasi" % dir)
    os.system("pause")

if __name__ == "__main__":
    main()