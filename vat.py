def getTotal(amount, sum, VAT):
    balance = sum - (amount * VAT)
    return balance

   
def userInput():
   
    amount = int(input(" Enter the total amount to be paid: "))  
    print("Total is: KES {0:.2f} ".format(amount))  

    sum = int(input(" Enter the amount paid:"))
    print("amount is: KES {0:.2f} ".format(sum))
    vat = float(input(" Enter the TAX rate:"))
    print("VAT is: KES {0:.2f} ".format(vat))

    balance = getTotal(amount, sum, vat)

    print("Your balance is: KES {0:.2f} ".format(balance))
    print(balance)


userInput()
