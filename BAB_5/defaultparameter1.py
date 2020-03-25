def cetak(alist=[], urut=False):
    if urut:
        alist.sort()
    for i in alist:
        print(i, end=' ')
    print()
    return

def main():
    li=[55,62,72,88,90,12]
    #memanggil fungsi cetak
    print("data tidak urut")
    cetak(li)
    print("data urut")
    cetak(li,True)

if __name__ == "__main__":
    main()