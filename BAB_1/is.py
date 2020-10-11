while True:
    print("Masukkan umur:")
    age = input()
    if age.isdecimal():
        break
    print("tuliskan umur dengan angka.")
while True:
    print("Buat password baru (dengan angka dan huruf):")
    password = input()
    if password.isalnum():
        break
    print("Password hanya bisa huruf dan angka.")
