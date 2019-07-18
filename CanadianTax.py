# income = input("Enter Your Income :")
# value1 = int(income)
 # definning Function
def taxForLow(parameter):
     incomeTax = int(parameter)
     baseAmount = incomeTax-0;
     fedralTax = baseAmount*0.15
     finalTax = fedralTax+0;
     return finalTax
#      # calling method
# # definning Function
def taxForMedium(parameter):
         incomeTax = int(parameter)
         baseAmount = incomeTax-47630;
         fedralTax = baseAmount*0.205
         finalTax = fedralTax+7145;
         return round(finalTax,2)
#           # calling method
# # definning Function
def taxForMediumU(parameter):
           incomeTax = int(parameter)
           baseAmount = incomeTax - 47630
           fedralTax = baseAmount*0.26
           finalTax = fedralTax+16908;
           return finalTax
#           # calling method
#
# # definning Function
def taxForMediumUpper(parameter):
          incomeTax = int(parameter)
          baseAmount = incomeTax-147667;
          fedralTax = baseAmount*0.29
          finalTax = fedralTax+30535;
          return finalTax
#           # calling method
#
# # definning Function
def taxForHighIncome(parameter):
          incomeTax = int(parameter)
          baseAmount = incomeTax-210371;
          fedralTax = baseAmount*0.33
          finalTax = fedralTax+48719;
          return finalTax
#           # calling method
def computing(value):
    result = 0;
    if value<47629 :
      result = taxForLow(value)

    elif value<95259:
     result = taxForMedium(value)

    elif value<147667:
     result = taxForMediumU(value)

    elif value<210371:
      result = taxForMediumUpper(value)

    else:
      result=taxForHighIncome(value)
    return result


print(computing(15000))
