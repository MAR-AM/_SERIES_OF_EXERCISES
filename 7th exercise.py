a=float(input('enter a : '))
b=float(input('enter b : '))
c=float(input('enter c : '))
d=b**2-4*a*c
if d<0:
    print('the equation did not have a solution!')
elif d==0:
    x=-b/(2*a)
    print('the solution is : ',x)
else:
    x1=(-b-d**0.5)/(2*a)
    x2=(-b+d**0.5)/(2*a)
    print('the solution are : ',x1,'et',x2)