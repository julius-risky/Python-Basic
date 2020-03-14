def main():
   #membuat input bilangan riil
   bilriil = float(input("masukkan bilangan riil: ")) 

   Hasil = bilriil * 5
   print(" bilangan yang dimasukkan adalah %f" %bilriil)
   print("%.2f + 5 = %.2f"%(bilriil,Hasil)) #%.2f mengambil 2 angka belakang koma

if __name__ == "__main__":
    main()
