def tambah(a,b):
    return a+b
def kurang(a,b):
     return a - b
def kali(a,b):
    return a*b
def bagi(a,b):
    return a/b

def main():
    a = float(input("masukkan bilangan ke-1: "))
    b = float(input("masukkan bilangan ke-2: "))
    op = input("masukkan operator \t:")

    d = {
        "+":tambah(a,b),
        "-":kurang(a,b),
        "*":kali(a,b),
        "/":bagi(a,b)
    }
    print("%.2f %s %.2f = %.2f"%(a,op,b,d[op]))

if __name__ == "__main__":
    main()
