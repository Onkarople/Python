#addition of two numbers using command line argumnets

from sys import *

def Add(No1,No2):
    Ans=0
    Ans=No1+No2
    return Ans

def main():
    print("welcome to:",argv[0])

    
    if(len(argv)==2):
        if(argv[1] == "--U"):
            print("use the application as:")
            print("python Name_Of_applications First_Number Second_Number")
            exit()

        if(argv[1] == "--H"):
            print("Help: this applications is used to perform addition of 2 numbers")
            exit()
    
    if(len(argv) !=3):
        print("invalid number of argumnets")
        print("please use --U flag to get usgae")
        exit()


   
        
    Ret=Add(int(argv[1]),int(argv[2]))
    print("Addition is:",Ret)
    print("Thank ypu for using Application by onkar ople")


if __name__== "__main__":
    main()
