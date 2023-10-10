A=float(input('Enter the first number : '))
B=float(input('Enter the second number : '))
if A*B>0:
    C=A
    A=B
    B=C
    print('The new value of A is : ',A)
    print('The new value of B is : ',B)
else:
    print('The new value of A is : ',A+B)
    print('The new value of B is : ',A*B)