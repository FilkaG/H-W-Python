#1
def SumOddNumners (List):
    Sum=0
    for i in range(1,len(List),2):
        Sum=Sum+List[i]
    return Sum

List=[2,3,4,5,8,7,5,6]
print('answer ', SumOddNumners(List))

#2
def MultiNumbers (List):
    AnswerList=[]
    for i in range(0,((len(List)+1)//2)):
        AnswerList.append(List[i]*List[len(List)-1-i])
    return AnswerList

List=[2,3,4,5,8,7,5,6]
print(MultiNumbers(List))
#3
ListFloat=[1.1,2.89,3.45]

def SubstrNumbers (List):
    max=round(List[0]-int(List[0]),10)
    min=round(List[0]-int(List[0]),10)
    const=0
    answer=0
    for i in range(1,len(List)):
        const=round(List[i]-int(List[i]),10)
        if const>max:
            max=const
        elif const<min:
            min=const
    answer=max-min     
    return answer

print(SubstrNumbers(ListFloat))

#5
def Fib (n):
    if n==0:
        F=0
    elif n==1:
        F=1
    else: F=Fib(n-1)+Fib(n-2)
    return F

def ListOfFib (n):
    AnswerList=[]
    for i in range(n,0,-1):
        AnswerList.append(-Fib(i))
    for i in range(0,n+1):
        AnswerList.append(Fib(i))
    return AnswerList

print(ListOfFib(7))

#4
def DoublSystem (number):
    Double=[]
    String=''
    while number//2!=0:
        Double.append(number%2)
        number=number//2
    Double.append(1)
    for i in range(len(Double)-1,-1,-1):
        String=String+str(Double[i])
    return String

print(DoublSystem(87))