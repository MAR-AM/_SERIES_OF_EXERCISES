n=int(input('Enter the value of n : '))
U0=6
for i in range (1,n):
  U=4*U0+10
  U0=U
print('U',n,'=',U)