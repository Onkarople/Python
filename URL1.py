import webbrowser
from sys import *
import os
import urllib.request
import re


def is_connected():
    try:
        urllib.request.urlopen('https://www.google.co.in/',timeout=1)
        return True
    except Exception as err:
        return False


def Find(string):
    url= re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',string)
    return url


def Launcher(path):
        with open(path,'r') as File:
            for line in File:
                print(line)
                url=Find(line)
                print(url)
                for str in url: 
                    webbrowser.open(str,new=2)
                   
      

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

    try:
        connected=is_connected()

        if connected:
            Launcher(argv[1])
        else:
            print("Unable to connect to internet")
    
    except ValueError:
        print("Error:Invalid datatype")
    except Exception as E:
        print("Error:Invalid Input",E)

if __name__=="__main__":
    main()