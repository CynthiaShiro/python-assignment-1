def getTotal(amount, sum, VAT):
    balance = sum - (amount * VAT)
    return balance

    # You could simplify this code by just  returning "sum - (amount * VAT)"


def userInput():
    # I renamed all variables starting with caps as they go against variable naming conventions in python
    amount = int(input(" Enter the total amount to be paid: "))  # Added closing bracket

    print("Total is: KES {0:.2f} ".format(amount))  # Python's format() function only takes one argument. To
    # format the output to 2dp, I added 0:.2f into the brackets used

    sum = int(input(" Enter the amount paid:"))
    print("amount is: KES {0:.2f} ".format(sum))
    vat = float(input(" Enter the TAX rate:"))
    print("VAT is: KES {0:.2f} ".format(vat))

    balance = getTotal(amount, sum, vat)

    print("Your balance is: KES {0:.2f} ".format(balance))
    print(balance)


userInput()
