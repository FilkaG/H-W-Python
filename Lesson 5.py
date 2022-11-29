#Task 1
def DelABC(string):
    str=string.split()
    str2=''
    for i in range (0,len(str)):
        if 'abc' in str[i]:
            str[i]=''

    for i in range (0,len(str)):
        if str[i]!='':
            str2=str2+str[i]+' '
    return str2

string = "abcfre qwe abc abc dfgj abcd rito dksj abc "
print(string)
print(DelABC(string))

#Task 2
numbersweet=200
name=[None]*2
name1=input('Print name of 1 player ')
name2=input('Print name of 2 player ')
count=1
print('START GAME!')
while numbersweet!=0:
    if count==1:
        name=name1
    else:
        name=name2
    print(f'Number of sweets---> {numbersweet}')
    minus=int(input(f'player {name} your turn!You can take no more 28 sweets---> '))
    if (minus>28 or minus<=0 or minus>numbersweet):
        print('You can not take this number of sweets! Try again!')
        count=count*(-1)
    else:
        numbersweet=numbersweet-minus
    if numbersweet==0:
        print(f'player {name} you WIN!')
    count=count*(-1)

#Task 2a,b
import random
numbersweet=2021
name=input('Print your name ')
print('START GAME!')
while numbersweet!=0:
    print(f'Number of sweets---> {numbersweet}')
    minus=int(input(f'player {name} your turn!You can take no more 28 sweets---> '))
    if (minus>28 or minus<=0 or minus>numbersweet):
        print('You can not take this number of sweets! Try again!')
    else:
        numbersweet=numbersweet-minus
        if numbersweet==0:
            print(f'player {name} you WIN!')
        else:
            print(f'Number of sweets---> {numbersweet}')
            print('My turn!')
            if (numbersweet>29 and numbersweet<=56):
                minus=numbersweet-29
                print(f'I will take {minus} sweets! ')
                numbersweet=numbersweet-minus
            elif numbersweet<=28:
                minus=numbersweet
                print(f'I will take {minus} sweets! ')
                numbersweet=numbersweet-minus
            else:
                minus=random.randint(1,29)
                print(f'I will take {minus} sweets! ')
                numbersweet=numbersweet-minus
            if numbersweet==0:
                print(f'I WIN!')

#Task 3
board=range(1,10)
def draw_game(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")

print('Для начала игры взгляните на игровое поле, цифры от 1 до 9 означают местооложение на поле. Для того,чтобы сделать ход, выберие номер соответствующий клетке, куда хотите сходить')
draw_game(board)
name1=input('Игрок 1, введите свое имя- ')
name2=input('Игрок 2, введите свое имя- ')
print('                 START GAME!')
board=[' ']*10
winner=''
count_name=1
count=1

while winner=='':
    print('         Ход игры:')
    draw_game(board)
    if count_name==1:
        name=name1
    else:
        name=name2
    number=int(input(F'Игрок {name} твой ход! '))
    if board[number-1]==' ':
        if name==name1:
            board[number-1]='X'
        else:
            board[number-1]='0'
    else:
        print('Это место уже занято, сходите иначе!')
        count_name=count_name*-1
    if ((board[0]==board[1]==board[2] and board[0]!=' ')  or (board[3]==board[4]==board[5] and board[3]!=' ') or (board[6]==board[7]==board[8] and board[6]!=' ') or (board[0]==board[3]==board[6] and board[0]!=' ') or (board[1]==board[4]==board[7] and board[1]!=' ') or (board[4]==board[5]==board[8] and board[4]!=' ') or (board[0]==board[4]==board[8] and board[0]!=' ') or (board[2]==board[4]==board[6] and board[2]!=' ')):
        winner=name
    
    if (count==9 and winner==''):
        winner='NO WINNER!'
    count_name=count_name*-1
    count+=1

draw_game(board)
print('           WINNER: ',winner)

#Task 4
def Rle_str(str):
    str=str+' '
    str2=''
    i=0
    while i<(len(str)-1):
        if str[i]==str[i+1]:
            j=i
            count=0
            const=str[i]
            while str[j]==const:
                count+=1
                j+=1
            str2=str2+(f'{const}:{count} ')
            i=i+count
        else:
            str2=str2+str[i]+' '
            i+=1
    return str2

def UnRle_str(str):
    str3=''
    str=str.split(' ')
    for i in range(len(str)-1):
        if ':' in str[i]:
            str3=str3+(str[i][:str[i].find(':')]*int(str[i][str[i].find(':')+1:]))
        elif (str[i]=='' and str[i+1]!=''):
            str3=str3+str[i]+' '
        else:
            str3=str3+str[i]
    return str3

f = open('file6.txt','r',encoding='UTF-8')
str=f.read()
f.close

f = open('file7.txt','w',encoding='UTF-8')
f.write(Rle_str(str))
f.close

f = open('file7.txt','r',encoding='UTF-8')
str=f.read()
f.close

f = open('file8.txt','w',encoding='UTF-8')
f.write(UnRle_str(str))
f.close