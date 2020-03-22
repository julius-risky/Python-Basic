def main():
    for i in range(10,25):
        prima = True
        for j in range (2,i):
            if i % j ==0:
                prima = False
                print(j)
                break
        if not prima:
            print("%d bukan prima"%i)
        else:
            print("%d bilangan prima"%i)

if __name__ == "__main__":
    main()