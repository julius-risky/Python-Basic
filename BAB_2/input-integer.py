nama = "arimbi"
umur = 21
print("nama: %s, umur: %d" % ("arimbi",21))
print("\n",100*"=")

def main():
    #membuat prompt untuk tipe data integer
    bil = int(input("masukkan bilangan bulat: "))
    hasil = bil + 11
    print("bilangan yang dimasukkan adala %d" %bil)
    print("%d + 11 = %d" %(bil,hasil)) 
    

if __name__ =="__main__":
    main()