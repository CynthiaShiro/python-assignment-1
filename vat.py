def getTotal(Amount,Sum,VAT):
    Balance=Sum-(Amount*VAT)
    return Balance
def UserInput():
    Amount=int(input(" Enter the total amount to be paid: ")
    print("Total is: KES {} ".format(Amount, ",.2f"))
    Sum=int(input( " Enter the amount paid:"))
    print("Amount is: KES {} ".format(Sum, ",.2f"))
    VAT=float(input( " Enter the TAX rate:")
    print("VAT is: KES {} ".format(VAT, ".2f"))
    Balance=getTotal(Amount,Sum,VAT)
    print("Your Balance is: KES {} ".format(Balance,",.2f"))
    print(Balance)
UserInput()

