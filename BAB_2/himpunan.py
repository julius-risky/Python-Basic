x = set([1,2,3,4,5])
y = set([4,3,6,7,8])


#union atau gabungan
a = x | y
print("gabungan: ", a)

#intersection atau irisan
b = x & y
print("irisan: ",b)

#difference atau selisih
c = x - y
print("selisih: ",c)

#symmetric difference
d = x ^ y
print("symmetric difference", d)