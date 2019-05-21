import math
Q = "√([(2 * C * D)/H])"
C = input('Nhap vao C')
print(C)
D = input('Nhap vao D')
print(D)
H = input('Nhap vao H')
print(H)
#replace thay the
Q = Q.replace('C',C).replace('D',D).replace('H',H)
Q = Q.replace('√','math.sqrt').replace('[','(').replace(']',')')
print(Q)
#chuyen doi doi tuong*
T = eval(Q)
print(T)
Q= 'Q='+Q
#chuyen doi doi tuong
S = exec(Q)
print(Q)
print(type(Q))