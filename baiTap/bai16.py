t=input('Nhap vao chuoi: ')
#ls=[]
#ln=[]
ls=0
ln=0
for i in t:
    try:
        int(i)
        #ln.append(i)
        ln+=1
    except ValueError:
        if i.isalpha():
            #ls.append(i)
            ls+=1
        else:
            pass
print('So: ', ln)#print(len(ln))
print('Chu: ', ls)#print(len(ls))