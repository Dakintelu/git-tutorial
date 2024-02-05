#Banking Application
accountno = 0
Cusname = " "
Bcode = " "
Mobile = 0
Bal = 0
def createaccount ():
    global accountno
    global Cusname
    global Bcode
    global Bal
    global Mobile
    accountno = int(input("Enter Account Number: "))
    Cusname = input("Enter Name: ")
    Bcode = input("Enter Branch Code: ")
    Mobile = int(input("Enter Mobile Number: "))
    Bal = int(input("Enter Current Balance: "))
def accountdetails ():
    print("Account No: " , accountno)
    print("Customer name" , Cusname)
    print("Branch code", Bcode)
    print("Mobile Number", Mobile)

def deposit(amount):
    global Bal
    Bal = Bal + amount
    checkbalance()
def withdraw(amount):
    global Bal
    Bal = Bal - amount
    checkbalance()
def checkbalance():
    global Bal
    print("Current Balance is:" , Bal)

#_Main_Menu_#
ch = "y"
while(ch =="y"):
    print("1. Create Account /2. Withdraw /3. Deposit /4. CheckBalance /5. Account Details ")
    ch = int(input("Select any option: "))
    if (ch == 1):
     createaccount()
    elif (ch == 2):
        amnt = int(input("Enter amount to withdraw: "))
        withdraw(amnt)
    elif (ch== 3):
        amnt = int(input("Enter amount to deposit: "))
        deposit(amnt)
    elif (ch == 4):
        checkbalance()
    elif (ch == 5):
        accountdetails()
    else:
        print("Please choose from the options above")
    print("To continue press y")
    ch = input()
