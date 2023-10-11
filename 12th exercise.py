N=int(input('Enter a number : '))
F=1
if N>0:
 for i in range (1,N+1):
   F=F*i
 print('the factorial is : ',F)
elif N==0:
 print('the factorial is : ',1)
else:
 print('Please enter a positive number !')