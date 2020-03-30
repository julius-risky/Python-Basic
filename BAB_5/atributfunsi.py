def kali(*daftar):
    """
        fungsi ini digunakan untuk mengalikan beberapa buah bilangan
    yang dilewatkan sebagai parameter
    """
    hasil = 1
    for nilai in daftar:
        hasil *= nilai
    return hasil
def main():
    print("kali(2,3,4)\t: ",kali(2,3,4))
    kali.nama = kali.__name__
    kali.doc = kali.__doc__
    kali.tgl = "30/03/2020"

    print("kali.nama\t: ",kali.nama)
    print("kali.doc\t:",kali.doc)
    print("kali.tgl\t:",kali.tgl)
    print(kali.__dict__)


