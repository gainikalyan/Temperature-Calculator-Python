#ATMOperations.py<---File Name and Module Name
from ATMExcept import DepositError,WithDrawError,InSuffFundError
bal=500.00 # Global Variable
def deposit():
    damt=float(input("Enter Ur Deposit Amount:")) # there is Possibility of raising ValueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tUr Account xxxxxxx123 Credited with INR:{}".format(damt))
        print("\tNow Ur Account xxxxxxx123 Balance after Deposit INR:{}".format(bal))

def withdraw():
    global bal
    wamt=float(input("Enter UR WithDraw Amount:")) # # there is Possibility of raising ValueError
    if(wamt<=0):
        raise WithDrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("\tUr Account xxxxxxx123 Debited with INR:{}".format(wamt))
        print("\tNow Ur Account xxxxxxx123 Balance After withdraw INR:{}".format(bal))

def balenq():
    print("\tUr Account xxxxxxx123 BalanceINR:{}".format(bal))
