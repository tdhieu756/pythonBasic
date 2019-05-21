s = "0100,0011,1010,1001"
s = s.split(',')
print(s)
l=[]
for i in s:
    if int(i)%5==0:
        l.append(i)
print(','.join(l))