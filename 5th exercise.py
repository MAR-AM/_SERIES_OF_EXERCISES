Age=int(input('Please enter the age of the resident : '))
gender=str(input('Please enter the gender of the resident : '))
if (gender=="man" and Age>=20) or (gender=="women" and Age>=18 and Age<=35):
    print('The resident is taxable.')
else:
    print('the resident is not taxable.')