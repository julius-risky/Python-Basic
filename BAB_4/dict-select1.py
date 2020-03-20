def main():
    hari = {1: "minggu",2: "senin",3: "selasa",4: "rabu",5: "kamis",6: "jum'at",7: "sabtu" }
    no = int(input("masukkan nomor hari: "))
    print("%d adalah hari %s"%(no,hari[no]))

if __name__ == "__main__":
    main()