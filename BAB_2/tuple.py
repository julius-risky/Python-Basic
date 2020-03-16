import datetime as dt

def main():
    bulan=("januari","februari","maret","april","mei","juni","juli","agustus","september","oktober","november","desember")

    today = dt.date.isoformat(dt.date.today())
    yyyy = today[:4]
    mm = today[5:7]
    dd = today[8:]
    print(today)
    print("%s %s %s"% (dd,bulan[int(mm)-1],yyyy))

if __name__ == "__main__":
    main()