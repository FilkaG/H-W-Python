import random

#1.1
number=(input('Print number '))
sum=0

for i in range(len(number)):
    if number[i]!='.':
        sum=sum+int(number[i])

print('answer sum=',sum)
#2.1
number_N=int(input('Print number N '))
answer=[i for i in range(number_N)]
answer[0]=1
count=2

for i in range(1,number_N):
    answer[i]=answer[i-1]*count
    count=count+1

print(answer)


##3.1
n_list=int(input('print N '))
List_of_function=[i for i in range(n_list+1)]
sum=0

for i in range(0,n_list+1):
    numb=random.randint(1,100)
    List_of_function[i]=(1+1/numb)**numb
    sum=sum+List_of_function[i]

print(round(sum,3))

##4.1
N=int(input('print N ')) 
List=[i for i in range(N)]
answer1=1

for i in range(0,N):
    List[i]=random.randint(-N-1,N+1)

print(List)

f = open('file.txt','r')
count_string=f.fileno()

for i in range(count_string):
    numer=int(f.readline())
    if numer<len(List):
        answer1=answer1*List[numer]
print('answer =',answer1)

#4.2 (используем список из 4.1)
for i in range(len(List)):
    countainer=List[i]
    count_container=random.randint(0,len(List)-1)
    List[i]=List[count_container]
    List[count_container]=countainer

print(List)