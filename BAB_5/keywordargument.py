def info(nama,usia,gaji):
    print("Nama : %s"%nama)
    print("Usia : %d"%usia)
    print("Gaji : %d"%gaji,end='\n\n')
    return

def main():
    info('bimo',25,4000000)
    info('juki',25,8000000)

if __name__ == "__main__":
    main()