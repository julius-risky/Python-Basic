import time

def hitungMundur(n):
    #li=[n]
    def next():
        nonlocal n
        r = n #n bisa diganti li[0]
        n -= 1
        return r
    return next


if __name__ == "__main__":
    main()