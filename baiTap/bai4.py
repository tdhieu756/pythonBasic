s = "34,67,55,33,12,98"
t = 't='+s
#ham chuyen doi doi tuong
exec(t)
print(t)
print(type(t))
l = list(t)
print(l)
print(type(l))
print('-------')
#ham chuyen doi doi tuong* trong ham con
c = eval(s)
print(c)
print(type(c))
v = list(c)
print(v)
print(type(v))