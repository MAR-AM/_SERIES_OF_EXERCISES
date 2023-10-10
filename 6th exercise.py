PHT=float(input('Please enter the price excluding the product tax : '))
Category=str(input('Please enter product category : '))
if Category==A:
    print('the price TTC of the product is : ',PHT*0.07+PHT,'DH')
elif Category==B:
    print('the price TTC of the product is : ',PHT*0.20+PHT,'DH')
elif Category==C:
    print('the price TTC of the product is : ',PHT*0.25+PHT,'DH')