def creatdic(x):
    dic = {}
    if x == 0:
        return dic
    else:
        for i in range(1,x+1):
            #add dic
            dic[i] = i*i
        return dic
x = int(input('Nhap vao so x: '))
print(creatdic(x))