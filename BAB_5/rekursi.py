import sys

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

def main():
    bil = int(input("Masukkan nilai faktorial yang anda inginkan: "))

    if bil < 0:
        print("EROR: Bilangan tidak boleh negatif")
        sys.exit(1)
    
    print("%d! \t= %d"%(bil,faktorial(bil)))

if __name__ == "__main__":
    main()