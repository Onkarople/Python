from sys import *
from os import *


def Script_Task(No):
    if(No%2==0):
        print("Its even Number")
    else:
        print("Its is Odd Number")



def main():
    print("----------------Marvellous Infosystems Automations------------")

    print("Automation script started with name :",argv[0])

    if(len(argv)!=2):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"): 
        print("Help: This script is used to perform __________")
    
    elif(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Provide ______ number of argumnets as")
        print("First Argument as _____")
        print("Second Argument as :_____")
        exit()

    else:
        Script_Task(int(argv[1]))
if __name__=="__main__":
    main()