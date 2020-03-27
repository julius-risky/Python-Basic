import time

def hitungMundur(n):
    #li=[n]
    def next():
        nonlocal n
        r = n #n bisa diganti li[0]
        n -= 1
        return r
    return next
 
def main():
    #memanggil fungsi hitungmundur
    a = int(input('masukkan waktu hitung mundur: '))
    next = hitungMundur(a)
    while True:
        val = next()
        if val == 0:
            print("Go..!!")
            break
        print(val, end=' ')
        time.sleep(0.1) #jeda waktu 1 detik

if __name__ == "__main__":
    main()