# mendefinisikan kelas node
class node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next


# mendefinisikan kelass linkedlist
class linkedlist:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def isEmpety(self):
        return self.size == 0

    def addfrist(self, element):
        if self.isEmpety():
            self.front = node(element)
            self.back = self.front
        else:
            temp = self.front
            self.front = node(element, temp)
        self.size += 1

    def addlast(self, element):
        if self.isEmpety():
            self.front = node(element)
            self.back = self.front
        else:
            self.back.next = node(element)
            self.back = self.back.next
        self.size += 1

    def printlist(self):
        print("isi linked list: ")
        current = self.front
        while current != None:
            print(current.element)
            current = current.next


def main():
    # membuat objek dari kelas linkedlist
    li = linkedlist()

    li.addfrist(input("masukkan nilai awal: "))
    # menambahkan elemen di awal

    # menambahkan elemen di akhir
    li.addlast(20)
    li.addlast(30)

    li.printlist()


if __name__ == "__main__":
    main()
