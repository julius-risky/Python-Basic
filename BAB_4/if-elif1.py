def main():
    bil = int(input("masukkan bilangan sesuka anda: "))

    if bil > 0:
        print("%d bilangan positif"%bil)
    elif bil == 0:
        print("% d adalah nol"%bil)
    else:
        print("%d bilangan negatif"%bil)
    
if __name__ == "__main__":
    main()