import random as rd
import datetime as dt
helloList =['Hi','Hello','Xin chao','Chao','Sawadi','hey']
nameList =['Hieu','Hai','Lan','Mi','Dung']
sexList =['nam', 'nu']
birthYear= list(range(1990,2000))
Now = dt.datetime.now()
yearNow = Now.year
giapList = ('Ti', 'Suu', 'Dan', 'Meo', 'Thin', 'Ty', 'Ngo', 'Mui', 'Than', 'Dau', 'Tuat', 'Hoi')
NowGiap = 'Hoi'

yearChoice =[
    'tuoi con %s' %(giapList((yearNow-birthYear)%12-giapList.index(NowGiap))),
    '%s tuoi'% (yearNow-birthYear)
]

print('%s %s %s, %s %s a?'%(
    rd.choice(helloList),
    rd.choice(sexList),
    rd.choice(nameList),
    rd.choice(sexList),
    
))