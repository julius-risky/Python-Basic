def tambah(*bil):
    hasil = 0
    for i in bil:
        hasil += i
    return hasil

def main():
    print("jumlah(3,4,5,6)\t\t: ",tambah(3,4,5,6))
    print("jumlah(5,6,7,8,9,10)\t: ",tambah(5,6,7,8,9,10))

if __name__ == "__main__":
    main()

    