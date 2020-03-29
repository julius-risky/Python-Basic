def jumlah(b1,b2,b3=None):
    if b3 == None:
        return b1 + b2
    else:
        return b1 + b2 + b3

def main():
    #memanggil fungsi jumlah
    print("jumlah (3,5) \t= ",jumlah(3,5))
    print("jumlah (4,5,6)\t= ",jumlah(4,5,6))

if __name__ == "__main__":
    main()