from sys import *
import os
import fnmatch
from glob import glob
from pathlib import Path
from shutil import copyfile

def DirectoryCopy(Directoryname,Dict_Name2):
    os.mkdir(Dict_Name2)

    flag=os.path.isabs(Directoryname)
    if flag==False:
        tempPath=os.path.abspath(Directoryname)
    
    exists=os.path.isdir(Directoryname)

    if exists:
        for foldername,subfolder,Filenames in os.walk(Directoryname):
      
            for fnames in Filenames:
                filepath = foldername
                src = os.path.join(filepath, fnames)
                dst = os.path.join(tempPath,fnames)
                copyfile(src, dst)
               
            

        
            print(" ")

       
        


def main():
    print("----------------Marvellous Infosystems Automations------------")

    print("Automation script started with name :",argv[0])

    if(len(argv)!=3):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"): 
        print("Help: This script is used to perform copy files from one folder to another")
    
    elif(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Provide 2 number of argumnets as")
        print("First Argument as Directory name")
        print("Second Argument as : Extension")

        exit()

    else:
        DirectoryCopy(argv[1],argv[2])

   
if __name__=="__main__":
    main()