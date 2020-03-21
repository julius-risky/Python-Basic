def main():
    i = 1
    while i <= 35:
        j=1
        while j <= i:
            print("%d "%(i*j),end=' ')
            j += 1 
        print()
        i += 1
    
if __name__ == "__main__":
    main()
