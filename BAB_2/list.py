def main():
    nilai = [100,200,300,400,500]

    #menampilkan elemen dalam list
    print("",nilai[0],"\n",nilai[1],"\n",nilai[2],"\n",nilai[3],"\n",nilai[4])
    print("\n",100*"=")
    print("",nilai[-1],"\n",nilai[-2],"\n",nilai[-3],"\n",nilai[-4],"\n",nilai[-5])
    #menambahkan data
    print("data awal: ",nilai)
    nilai.append(600)
    print("nilai sesudah append():", nilai)
    nilai.insert(7,900)
    print("sesudah nilai.insert():",nilai)
    nilai.extend([('buah'),1000])
    print("nilai sesudah extend()",nilai)
    #mengubah nilai
    nilai[0]=10
    print("sesudah diubah: ",nilai)
    #mencari indeks
    a = nilai.index(500)
    print("500 berada pada indeks %d" %a)
    #menghapus nilai list
    nilai.remove(200)
    nilai.remove('buah')
    del nilai[5]
    print("nilai setelah dihapus: ",nilai)
    nilai.pop(0)
    print("menghapus dengan pop: ",nilai)
    nilai.clear()
    print("menghapus semua isi list: ",nilai)

if __name__ == "__main__":
    main()