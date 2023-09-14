#object oriented concept
#instace Variable:-Name,Amount,Address,Account Number
#Instance Methods:- CreateAccount,DisplayAccountInfo
#class Variable:-Bank name.ROI On FD

import random

class Bank_Account:
    Bank_Name="HDFC Bank PVT LTD"
    ROI_On_FD=6.7

    def __init__(self):
        self.Name=""
        self.Amount=0
        self.Address=""
        self.AccountNo=random.randint(0,100)
    
    def CreateAccount(self):
        print("Enter your name")
        self.Name=input()

        print("Enter your initail amount")
        self.Amount=int(input())

        print("Enter your Address")
        self.Address=input()

        
    def DisplayAccountInfo(self):
        print("..........Your account information as Below........")
        print("Name of Account Holder:",self.Name)
        print("Account Number:",self.AccountNo)
        print("Address of account Holder:",self.Address)
        print("Current Amount in Account:",self.Amount)

def main():
    print("Name of Bank :",Bank_Account.Bank_Name)
    print("Rate of inetrest on FD is {} %:".format(Bank_Account.ROI_On_FD))

    User1=Bank_Account()
    User2=Bank_Account()

    print("Creating the first account")

    User1.CreateAccount()

    print()

    User1.DisplayAccountInfo()

    print()

    print("Creating the Second account")

    User2.CreateAccount()
    print()

    User2.DisplayAccountInfo()



if __name__ == "__main__":
    main()
