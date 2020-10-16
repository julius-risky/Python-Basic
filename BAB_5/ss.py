def kode (A,B):
    if A < B:
        print('er')
    elif A < 10:
        return A + B
    elif A > 100:
        return A / B
    else:
        return A * B 

def main():
    print(kode(10,10))
    print(kode(180,9))
    print
if __name__ == "__main__":
    main()