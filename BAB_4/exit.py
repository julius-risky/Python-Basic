import sys
def main():
    print("program pembagian bilangan")
    a = float(input("\n masukkan nilai a: "))
    b = float(input("\n masukkan nilai b: "))

    if b == 0.0:
        print("kesalahan b tidak boleh nol")
        sys.exit(1)

    c =a / b
    print("%.2f / %.2f = %.2f"%(a,b,c))

if __name__ == "__main__":
    main()