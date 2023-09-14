#addition of two numbers using command line argumnets

from sys import *

def Add(No1,No2):
    Ans=0
    Ans=No1+No2
    return Ans

def main():
    if(len(argv)!=3):
        print("invalid number of argumnets")
        exit()
        
    Ret=Add(int(argv[1]),int(argv[2]))
    print("Addition is:",Ret)


if __name__== "__main__":
    main()
