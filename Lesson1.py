#1.1
day=int(input('print number of the day '))
if (day==6 or day==7):
    print('holiday')
else:
    print('not holiday')

#2.1
X=0
Y=0
Z=0
print(f'X={X} Y={Y} Z={Z}')
print('¬X1∧¬X2∧¬X3=',(not X) and (not Y) and (not Z))
print('¬(X1∨X2∨X3)=',not(X or Y or Z))

X=0
Y=0
Z=1
print(f'X={X} Y={Y} Z={Z}')
print('¬X1∧¬X2∧¬X3=',(not X) and (not Y) and (not Z))
print('¬(X1∨X2∨X3)=',not(X or Y or Z))

X=0
Y=1
Z=0
print(f'X={X} Y={Y} Z={Z}')
print('¬X1∧¬X2∧¬X3=',(not X) and (not Y) and (not Z))
print('¬(X1∨X2∨X3)=',not(X or Y or Z))

X=0
Y=1
Z=1
print(f'X={X} Y={Y} Z={Z}')
print('¬X1∧¬X2∧¬X3=',(not X) and (not Y) and (not Z))
print('¬(X1∨X2∨X3)=',not(X or Y or Z))

X=1
Y=0
Z=0
print(f'X={X} Y={Y} Z={Z}')
print('¬X1∧¬X2∧¬X3=',(not X) and (not Y) and (not Z))
print('¬(X1∨X2∨X3)=',not(X or Y or Z))

X=1
Y=0
Z=1
print(f'X={X} Y={Y} Z={Z}')
print('¬X1∧¬X2∧¬X3=',(not X) and (not Y) and (not Z))
print('¬(X1∨X2∨X3)=',not(X or Y or Z))

X=1
Y=1
Z=0
print(f'X={X} Y={Y} Z={Z}')
print('¬X1∧¬X2∧¬X3=',(not X) and (not Y) and (not Z))
print('¬(X1∨X2∨X3)=',not(X or Y or Z))

X=1
Y=1
Z=1
print(f'X={X} Y={Y} Z={Z}')
print('¬X1∧¬X2∧¬X3=',(not X) and (not Y) and (not Z))
print('¬(X1∨X2∨X3)=',not(X or Y or Z))

#2.2
X=int(input('Print X='))
Y=int(input('Print Y='))

if X>0 and Y>0:
    print('first')
elif X<0 and Y>0:
    print('second')
elif X<0 and Y<0:
    print('Third')
elif X>0 and Y<0:
    print('fourth')

#3.1
quarter=int(input('Print quarter='))

if quarter==1:
    print('X=(0;+∞) Y=(0,+∞)')
elif quarter==2:
    print('X=(-∞,0) Y=(0,+∞)')
elif quarter==3:
    print('X=(-∞,0) Y=(-∞,0)')
elif quarter==4:
    print('X=(0;+∞) Y=(-∞,0)')

#3.2
print('print coordinates A')
X_A=int(input('X='))
Y_A=int(input('Y='))

print('print coordinates B')
X_B=int(input('X='))
Y_B=int(input('Y='))

print('AB=',((X_B-X_A)**2+(Y_B-Y_A)**2)**0.5)