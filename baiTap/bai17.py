st = input('Nhap chuoi: ')
S=0
s=0
x=0
for i in st:
    if i.isupper():
        S+=1
    elif i.isalpha():
        s+=1
    else:
        x+=1
print('Low ', s, '   and High ',S , '    Space ',x)