def tambah(a,b):
    c = a+b
    return c

def main():
    x = int(input("masukkan nilai ke-1: "))
    y = int(input("masukkan nilai ke-2: "))

    hasil = tambah(x,y)
    print("%d + %d = %d"%(x,y,hasil))

if __name__ == "__main__":
    main()