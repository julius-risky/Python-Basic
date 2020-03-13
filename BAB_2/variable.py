import random
import statistics

def main():
    #membuat variable
    x = random.sample(range(80,120),30)
    y = 1.664
    z = statistics.mean(x)
    a = y * z
    bahasa = "hallo kamu"
    kalimat = " apa kabar"

    #menampilkan nilai variable ke layar
    print(x)
    print(y)
    print(z)
    print(a)
    print(bahasa+kalimat)

if __name__ == "__main__":
    main()
    