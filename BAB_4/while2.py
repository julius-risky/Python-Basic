def main():
    #melakukan pengulangan dari a ke e
    ch = 'a'
    while ch <= 'e':
        print("%c : hello world!"%ch)
        ch = chr(ord(ch)+1)
    
if __name__ == "__main__":
    main()

for y in 'python':
    print(y)