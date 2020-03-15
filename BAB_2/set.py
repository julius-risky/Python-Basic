import sys

def printElements(s, info):
    print(info)
    if len(s) == 0:
        print("himpunan kosong\n")
        sys.exit(1)
    for e in s:
        print(str(e)+" ", end=' ')
    print("\n")

def main():
    #membuat himpunan
    s = set([11,22,33,44,55])
    printElements(s, "elemen awal:")

    #menambah anggota/elemen baru
    #metode add
    s.add(66)
    s.add(77)
    printElements(s,"setelah panggilan add(): ")
    
    #metode update()
    s.update([88,99])
    printElements(s,"setelah panggilan update()")
    #menghapus
    s.remove(11)
    printElements(s,"seteleh s.remove(): ")

    #menghapus semua anggota
    s.clear()
    printElements(s, "setelah clear()")


if __name__ == "__main__":
    main()