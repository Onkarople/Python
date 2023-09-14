import subprocess
import webbrowser
from sys import *
import os
import urllib.request
import re


def Launcher(Filename):
    flag=os.path.isabs(Filename)
    if flag==False:
        Filename=os.path.abspath(Filename)
    
    exists=os.path.isfile(Filename)

    if exists:
        with open(Filename,'r') as File:
            for line in File:
                urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
                print(urls)
                webbrowser.open(urls,new=2)
    
    else:
        print("invalid path")
   

   
   

def main():
    print("----------------Marvellous Infosystems Automations------------")

    print("Automation script started with name :",argv[0])

    if(len(argv)!=2):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"): 
        print("Help: This script is used to perform open url in new tab")
    
    elif(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Provide one number of argumnets as")
        print("First Argument as filename")
       
        exit()

    else:
        Launcher(argv[1])
        print("End")


if __name__=="__main__":
    main()