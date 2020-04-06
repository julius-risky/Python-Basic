import math

class hitung(object):
    def __init__(self,p,l,t):
        pass

    @staticmethod
    def log10(x):
        return math.log10(x)

    @staticmethod
    def log(x):
        return math.log(x)
    
    @staticmethod
    def kali(x,y):
        return x * y

    @staticmethod
    def pangkat(x,y):
        return math.pow(x,y)
    
    @staticmethod
    def akar(x):
        return math.sqrt(x)
    
    @staticmethod
    def mutlak(x):
        return abs(x)

def main():
    print("hitung.log10(1000): %.2f"%hitung.log10(1000))
    print("hitung.log(500): %.2f"%hitung.log(500))
    print("hitung.kali(6,7): %.2f"%hitung.kali(6,7))
    print("hitung.akar(81): %.2f"%hitung.akar(81))
    print("hitung.mutlak(-10): %.2f"%hitung.mutlak(-10))
    print("hitung.pangkat(2,5): %.2f"%hitung.pangkat(2,5))
if __name__ == "__main__":
    main()