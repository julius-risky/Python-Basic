def main():
    print("Masukkan nilai koordinat")
    x = int(input("masukkan nilai x: "))
    y = int(input("masukkan nilai y: "))

    info = "koordinat ("+ str(x)+","+ str(y) +\
        ") berada pada kuadran "
    
    if x > 0 and y > 0:
        print(info +"I")
    elif x < 0 and y > 0:
        print(info +"II")
    elif x < 0 and y < 0:
        print(info+ "III")
    elif x > 0 and y <0:
        print(info+"IV")
    else:
        pass
    

if __name__ == "__main__":
    main()