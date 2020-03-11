import os, py_compile

def main():
    os.chdir("F:\\python-buku_budi_raharjo\\BAB_1")
    py_compile.compile("hello.py")
    print("file hello.pyc telah dibuat...")
    os.system("pause")

if __name__ == "__main__":
    main()