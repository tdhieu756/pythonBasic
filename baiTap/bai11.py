t = 'without,hello,bag,world'
#splip la ham tach str sang list voi ky tu mac dinh la " "
x = t.split(',')
#sort la sap sep lai list
x.sort()
#join ham tron ly tu vao
print(','.join(x))
