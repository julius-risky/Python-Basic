def ubahnilai(p):
    print("\n nilai Didalam fungsi")
    p *= 100
    print("p\t= %d"%p)
    return

def main():
    a = 5
    print("sebelum fungsi ubahnilai")
    print("a \t= %d"%a )

    #mengambil fungsi ubahnilai
    #dengan a sebagai parameter aktualnya
    ubahnilai(a)
    print("\n Setelah pemanggilan fungsi")
    print("a\t= %d"%a)

if __name__ == "__main__":
    main()