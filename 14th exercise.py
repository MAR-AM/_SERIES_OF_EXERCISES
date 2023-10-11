n=int(input('Enterc a number : '))
if n>0:
 for i in range(1,n):
     if n%i==0:
         print(i,'is a divisor of',n)
else:
    print("Please enter a positive number!")