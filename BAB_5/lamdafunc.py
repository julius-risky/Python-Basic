#mendefinisikan fungsi pemanggil
#parameter dan nilai kebalian berupa fungsi
def panggil(func):
    return func

def helloword():
    return "Hello world"

def main():
    #mendefinisikan list
    daftarnama =["Dewi","bimo","Aji","BAYU","sakit"]
    print("keadaan awal: ")
    print(daftarnama)

    #mengurutkan elemen list dengan dhorted()
    print("\nMenggunakan sorted(): ")
    print(sorted(daftarnama))

    #melewatkan lambda func untuk mengurutkan
    #elemen tanpa memperdulikan huruf kecil/besar
    daftarnama.sort(key=lambda n: n.lower())

    print("\nkeadaan akhir: ")
    print(daftarnama)

if __name__ == "__main__":
    main()
    