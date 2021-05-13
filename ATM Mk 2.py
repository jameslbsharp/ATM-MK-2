from decimal import * 
balance = 100


def check_balance_validity(wd):
    try:
        val = int(wd)
        check_qty(wd)
    except ValueError:
        print (" ")
        print("INVALID ENTRY")
        print (" ")
        print (" ")
        withdrawls_and_deposits_initial(balance)

def check_qty(wd):
    if int(wd) > int(balance):
        print (" ")
        print("ERROR: Account balance exceeded")
        print (" ")
        withdrawls_and_deposits_initial(balance)
    else:
        return

def withdrawls_and_deposits_initial (balance):
    print ("Your balance is", balance)
    print (" ")
    print (" ")
    wd = (input ("Please enter how much you would like to deposit or withdraw "))
    check_balance_validity(wd)
    wd = int(wd)
    balance = int(balance)
    balance += wd
    print (" ")
    print ("Your balance is now", balance)
    print (" ")
    wap_second (balance)
          
def wap_second (balance):
    cont = input("Would you like to continue? yes/return to menu ")
    print (" ")
    ContFirstLetter = cont[0].lower()
    if ContFirstLetter == "y":
        withdrawls_and_deposits_initial(balance)
        #wap_second(balance)
    elif ContFirstLetter == "r":
        main_menu(balance)
    else:
        print("Invalid response, please try again")
        print (" ")
        print (" ")
        wap_second(balance)

## 4. Loan calc ##

def loan_calc(balance):
    print (" ")
    print (" ")
    a = input("How much would you like to borrow from us? ")
    b = input("How many months would you like to pay it back ")
    a = float(a) # initial payment
    b = float(b) # length of payment

    if a <= 1000:
        loan_agreement = input("we offer 0.005% interest p/m for loans that size, are you happy with that? Yes/No ")
        loan_agreement_first_letter = loan_agreement[0].lower()
        n = 0.005 # monthly repayment of echelon 1
        n = float(n)
        if loan_agreement_first_letter == "y":
            q = (a*(n*((1+n)**b)))/(((1+n)**b)-1)
            q = round(q,2)
            print("Your monthly repayment will be £{}".format(q))
            print("Your money has been deposited in your account, returning you to menu")
            balance = balance + a  
            print (balance)
            main_menu(balance)
        elif loan_agreement_first_letter == "n":
            r = input("Would you like to select another option or return to main menu? Yes/Return ")
            rfl = r[0].lower()
            if rfl == "y":
                loan_calc()
            elif rfl == "r":
                main_menu()
    
    if a > 1000 and a <= 9999:
        loan_agreement = input("we offer 0.008% interest p/m for loans that size, are you happy with that? Yes/No ")
        loan_agreement_first_letter = loan_agreement[0].lower()
        n = 0.008 # monthly repayment of echelon 2
        n = float(n)
        if loan_agreement_first_letter == "y":
            q = (a*(n*((1+n)**b)))/(((1+n)**b)-1)
            q = round(q,2)
            print("Your monthly repayment will be £{}".format(q))
            print("Your money has been deposited in your account, returning you to menu")
            balance = balance + a  
            print (balance)
            main_menu(balance)
        elif loan_agreement_first_letter == "n":
            r = input("Would you like to select another option or return to main menu? Yes/Return ")
            rfl = r[0].lower()
            if rfl == "y":
                loan_calc()
            elif rfl == "r":
                main_menu()
    
    if a > 10000:
        loan_agreement = input("we offer 0.001% interest per month for loans that size, are you happy with that? Yes/No ")
        loan_agreement_first_letter = loan_agreement[0].lower()
        n = 0.001 # monthly repayment of echelon 2
        n = float(n)
        if loan_agreement_first_letter == "y":
            q = (a*(n*((1+n)**b)))/(((1+n)**b)-1)
            q = round(q,2)
            print("Your monthly repayment will be £{}".format(q))
            print("Your money has been deposited in your account, returning you to menu")
            balance = balance + a  
            print (balance)
            main_menu(balance)
        elif loan_agreement_first_letter == "n":
            r = input("Would you like to select another option or return to main menu? Yes/Return ")
            rfl = r[0].lower()
            if rfl == "y":
                loan_calc()
            elif rfl == "r":
                main_menu()


## 3. Lets customer view balance incl. option to withdraw or to return to menu ## 


def display_balance(balance):
        print("")
        print("")
        print("Your balance is", balance)
        print("")
        print("")
        display_balance_continue(balance)
        
def display_balance_continue(balance):
    Z = input("Do you wish to make a deposit or withdrawl, if not return to menu? Type Yes/Return ")
    Zfirstletter = Z[0].lower()
    if Zfirstletter == "y":            
        withdrawls_and_deposits_initial(balance)

    elif Zfirstletter == "r":
        main_menu(balance)
    else:
        print("")
        print("")
        print("Invalid entry")
        display_balance_continue()

## 2. Opening menu customer sees after entering in their pin ##

def main_menu(balance):
    print("")
    print("")
    print("Type N to")
    print("[1] View Balance")
    print("[2] Make Withdrawls")
    print("[3] View our loans")
    print("[4] to exit")
    M = input(" ")
    M = int(M)
    if M == 1:
        display_balance(balance)
    elif M == 2:
        withdrawls_and_deposits_initial (balance)
        #wap_second(balance)
    elif M == 3:
        loan_calc(balance)
    elif M == 4:
        print("Have a nice day.")
        exit()
    else:
        print("Invalid entry, please try again")
        main_menu()


## 1. Verifies pin before moving on to main menu ##

pin = 1234
   
def ask_pin(count):
    pin_entry = input ("Please enter your PIN ")
    pin_entry = int(pin_entry)

    if pin_entry == pin:
        main_menu(int(balance))
    
    elif pin_entry != pin and count < 2:
        count += 1
        print("")
        print("")
        print("Incorrect, {} remaining attempts".format(3-count))
        print("")
        print("")
        ask_pin(count)

    else:
        print("")
        print("")
        print("Account locked")
        print("")
        print("")
        exit()

print (" ")
print (" ")
print ("Welcome")
print (" ")


ask_pin(0)

########################


