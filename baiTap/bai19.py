s = '1,2,3,4,5,6,7,8,9'
t=eval(s)
print(t)
tl=()
for i in t:
    if i%2!=0:
        tl = tl + (i,)
print(tl)