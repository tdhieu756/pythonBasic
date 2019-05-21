x = int(input('Nhap X '))
y = int(input('Nhap Y '))
l = []
print(l)
for i in range(x):
    c =[]
    for j in range(y):
        #them vao cuoi list
        c.append(j*i)
    l.append(c)
print(l)