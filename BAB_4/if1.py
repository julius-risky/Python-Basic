def main():
    bilangan = int(input("masukkan bilangan yang anda mau: "))

    if bilangan % 2 == 0:
        print("%d bilangan genap "% bilangan)
    else:
        print("%d bilangan ganjil"%bilangan)

if __name__ == "__main__":
    main()