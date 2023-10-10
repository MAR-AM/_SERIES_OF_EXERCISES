N=int(input('Type the number of photocopies : '))
if N<=10:
    print('The invoice is : ',N*0.30,'DH')
elif N>10 and N<=30:
    print('The invoice is : ',10*0.30+(N-10)*0.25,'DH')
else:
    print('The invoice is : ',10*0.30+20*0.25+(N-30)*0.20,'DH')