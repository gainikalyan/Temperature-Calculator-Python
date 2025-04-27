#ATMOperationsDemo.py<---Main Program
from ATMExcept import DepositError, WithDrawError, InSuffFundError
from ATMMenu import menu
from ATMOperations import deposit, withdraw, balenq
while(True):
    menu()
    try:
        ch=int(input("Enter UR Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("\tDon't try to Deposit alnums,strs,symbols")
                except DepositError:
                    print("\tDon't enter -ve and zero as Deposit amount:")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("\tDon't try to Withdraw alnums,strs,symbols")
                except WithDrawError:
                    print("\tDon't enter -ve and zero as withdraw amount:")
                except InSuffFundError:
                    print("\tUR Account does not contain suff. funds--read python notes")
            case 3:
                balenq()
            case 4:
                print("Thx for this Project")
                break
            case _:
                print("\tUr Selection of Operation is Wrong-try again")
    except ValueError:
        print("\tDon't enter alnums,strs and symbols--try again")