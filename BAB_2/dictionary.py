def main():
    #membuat dan mengisi nilai ke dalam dictionary
    d = {'nama':'julius','Nim':161414099,'alamat':'minggir'}
    print("data asli:",d)
    #menambahkan data
    d['Nilai']='A' 
    d['hobi']= 'menonton anime'
    #menampilkan dictionary
    print("data tambahan :",d)
    #memodifikasi data
    d['nama']=input("\nnama kamu: ") 
    d['Nim']=input("Tulis Nim kamu: ")
    d['hobi']=input("tulis hobimu: ")
    print("\ndata sesudah di modif :",d)

    #menghapus elemen dari dictionary
    del d['alamat']
    print("update data: ",d)

if __name__ == "__main__":
    main()
    