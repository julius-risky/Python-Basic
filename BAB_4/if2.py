def main():
    namahari=("minggu","senin","selasa","rabu","kamis","jumat","sabtu")

    hari = input("masukkan nama hari: ")

    if hari.lower() == namahari[0] or\
        hari.lower() == namahari[6]:
        print("%s adalah hari libur"%hari)
    else:
        print("%s tetap masukk kuliah"%hari)

if __name__ == "__main__":
    main()