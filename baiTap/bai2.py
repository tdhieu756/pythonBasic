def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
z = int(input('so giai thua!'))
print('ket qua giai thua %d la: %d' %(z,fact(z)))