def cetak(*var):
    for i in var:
        print("",i,end=' ')
    
def main():
    #memanggil fungsi
    print("satu parameter")
    cetak(10)
    print("\n Dua parameter")
    cetak(15,18)
    print("\n Tiga parameter")
    cetak(14,10,5)
if __name__ == "__main__":
    main()