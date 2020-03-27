#mendefinisikan fungsi pemanggil dengan
#parameter dan nilai kembalian berupa fungsi
def panggil(func):
    return func

#mendefinisikan fungsi
def hello():
    print("hello world!!")

def main():
    #memangil fungsi panggil() dengan melewatkan
    #fungsi hello() sebagai argumennya
    s = panggil(hello())
    print(s)

if __name__ == "__main__":
    main()