from sys import *
import os
import fnmatch
from glob import glob
from pathlib import Path
from shutil import copyfile

def DirectoryCopyExt(Directoryname,Dict_Name2,Ext):
    os.mkdir(Dict_Name2)

    flag=os.path.isabs(Dict_Name2)
    if flag==False:
        tempPath=os.path.abspath(Dict_Name2)
    
    exists=os.path.isdir(Dict_Name2)

    if exists:
        for foldername,subfolder,Filenames in os.walk(Directoryname):
      
            for fnames in Filenames:
                s=fnames.split('.')

                if s[1]==Ext[1:]:
                 filepath = foldername
                 src = os.path.join(filepath, fnames)
                 dst = os.path.join(tempPath,fnames)
                 copyfile(src, dst)
               
            

        
            print(" ")
    else:
        print("invalid path")

       
        


def main():
    print("----------------Marvellous Infosystems Automations------------")

    print("Automation script started with name :",argv[0])

    if(len(argv)!=4):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"): 
        print("Help: This script is used to perform copy files from one folder to another of given extensions")
    
    elif(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Provide 2 number of argumnets as")
        print("First Argument as Directory name")
        print("Second Argument as Directory name")

        print("Third Argument as : Extension")

        exit()

    else:
        DirectoryCopyExt(argv[1],argv[2],argv[3])

   
if __name__=="__main__":
    main()