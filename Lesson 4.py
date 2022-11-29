#Task 1
d=0.001

def rounding(number,d):
    count=0
    while d<1:
        count=count+1
        d=d*10
    number=round(number,count)
    return number

print(rounding(3.145674,d))

#Task 2
n=12376

def SimpleFactor(n):
    list=[]

    if n%2==0:
        list.append(2)
    elif n%3==0:
        list.append(3)
    if n>=5:
        for i in range (6,n,6):
            if n%(i-1)==0:
                list.append(i-1)
            elif n%(i+1)==0:
                list.append(i+1)
    return list

print(SimpleFactor(n))

#Task 3
list =[1,1,34,678,67,567,888,3466,232,2,1,4,0,0.1,0,233,3466,233,5,-10,345,22,2,1,45]

def NoMore(list):
    answer=[]
    for i in range(0,len(list),1):
        count=0
        for j in range(0,len(list),1):
            if list[j]==list[i]:
                count=count+1
        if count<2:
            answer.append(list[i])
    return answer

print(NoMore(list))
#Task 4
import random

k=int(input('print k '))
def Poly(k):
    str=''
    while k!=0:
        coef=random.randint(0,101)
        if coef!=0:
            str= str+ f"{coef}*x^{k} + "
            k=k-1
    coef=random.randint(0,101)
    if coef==0:
        str=str[:-1]
        str=str+f" = 0"
    else:
        str=str+f"{coef} = 0"
    return str

f = open('file2.txt','w')
f.write(Poly(k))
f.close

##Task5
f = open('file3.txt','r')
str1=f.read()
f.close
str1=str1[:-4]
print('first poly-->',str1)

f = open('file4.txt','r')
str2=f.read()
f.close
str2=str2[:-4]
print('Second poly-->',str2)

#delim stroky
def NewString(str):
    strSp=str.split(' + ')
    return(strSp)

#yznaem stepen
def StepPoly(str):
    if 'x' in str:
        step=int(str[str.find('^')+1:str.find(' ')])
    else:
        step=0
    return step

#sozdaem spisok koefizientov
def CoefStr(str1Sp,step):
    coef=[0]*(step+1)
    for i in range(0,len(str1Sp)):
        st=StepPoly(str1Sp[i]+' ')
        if 'x' in str1Sp[i]:
            coef[st]=int(str1Sp[i][:str1Sp[i].find('*')])
        else:
            coef[st]=int(str1Sp[i])
    return coef

#Summa polynomov
def SumPoly(str1,str2):
    str1Sp=NewString(str1)
    str2Sp=NewString(str2)
    step1=StepPoly(str1)
    step2=StepPoly(str2)
    coef1=CoefStr(str1Sp,step1)
    coef2=CoefStr(str2Sp,step2)
    if len(coef2)>len(coef1):
        lencoef3=len(coef2)
        coef1=coef1+[0]*(len(coef2)-len(coef1))
    else:
        lencoef3=len(coef1)
        coef2=coef2+[0]*(len(coef1)-len(coef2))
    coef3=[0]*lencoef3
    for i in range(0,lencoef3):
        coef3[i]=coef2[i]+coef1[i]
    str3=''
    for i in range(7,0,-1):
        if coef3[i]!=0:
            str3=str3+f'{coef3[i]}*x^{i} + '
    if coef3[0]==0:
        str3=str3[:-2]
        str3=str3+'= 0'
    else:
        str3=str3+f'{coef3[0]} = 0'
    return str3

f = open('file5.txt','w')
f.write(SumPoly(str1,str2))
f.close

