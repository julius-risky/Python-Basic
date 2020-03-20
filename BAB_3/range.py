def printlist(li):
    for e in li:
        print(e, end=' ')
    print()

def main():
    bilangan = range (30)
    genap = []
    ganjil = []

    for x in bilangan:
        if x % 2 == 0:
            genap.append(x)
        else:
            ganjil.append(x)
    print("bilangan genap\t:",end='')
    printlist(genap)
    print("bilangan hanjil\t:",end='')
    printlist(ganjil)

if __name__ == "__main__":
    main()