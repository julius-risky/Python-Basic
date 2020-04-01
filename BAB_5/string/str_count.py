def main():
    str = "hello world!!"
    a = str.count('l')
    b = str.count('o')
    c = str.count('l',1,6)

    print("Huruf 'l' dalam str: ",a)
    print("huruf 'o' dalam str: ",b)
    print("huruf 'l' dari indeks 1-6: ", c)


if __name__ == "__main__":
    main()