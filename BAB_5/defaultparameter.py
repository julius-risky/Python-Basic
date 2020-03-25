def infokaryawan(nama,usia=35):
    print("nama: %s"%nama)
    print("usia: %d"%usia, end='\n\n')
    return

def main():
    #memanggil nama karyawan
    infokaryawan("bimo") #mengisi usia sesuai parameter default
    infokaryawan("haryo",33)
    infokaryawan("juki",22)

if __name__ == "__main__":
    main()