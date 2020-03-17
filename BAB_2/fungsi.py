def modulo(a,b):
    hasil = a % b
    return hasil


h1 = modulo(10,3)
print(h1)

#=========================================================
print(100*"=")

import datetime as dt 

def getisoformat(date):
    return dt.date.isoformat(date)

def day(date):
    datestr = getisoformat(date)
    return int(datestr[8:])

def month(date):
    datestr = getisoformat(date)
    return int(datestr[5:7])

def year(date):
    datestr = getisoformat(date)
    return int(datestr[:4])

def main():
    bulan=("januari","februari","maret","april","mei","juni","juli","agustus","september","oktober","november","desember")
    today = dt.date.today()
    print(getisoformat(today))
    print(day(today),bulan[int(month(today)-1)],year(today))
    print(day(today)) 
    print(month(today))
    print(year(today))
if __name__ == "__main__":
    main()