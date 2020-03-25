def ubahnilai(p):
    print("\ndidalam fungsi")
    print("p lama \t\t: %d"%p)
    print("ID P lama\t: %d"%id(p))

    
def main():
    a = 5
    print("sebelum pemanggilan fungsi")
    print("ID a \t\t: %d"%id(a))

    #memanggil fungsi ubah nilai
    ubahnilai(a)
    print("\n setelah pemanggilan fungsi")
    print("a \t\t: %d"%a)
    print("ID A \t\t: %d"%id(a))

if __name__ == "__main__":
    main()