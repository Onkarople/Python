import os 
from sys import *
import re
from shutil import copyfile


def Directory_Watcher(Dir_name,NewName):
    print("Inside directory watcher method")
    print("Name of Input Directory : ",Dir_name)

    os.mkdir(NewName)
    tempPath=os.path.abspath(NewName)

    flag=os.path.isabs(Dir_name)
    if flag==False:
        Dir_name=os.path.abspath(Dir_name)
    
    exists=os.path.isdir(Dir_name)
   

    if exists:


        for foldername,subfolder,Filenames in os.walk(Dir_name):
            print("Folder name is : "+foldername)
            for fnames in Filenames:
                with open(os.path.join(foldername,fnames),'r') as file:
                    for line in file:
                        for m in re.findall(r"\bsex\b|\bporn\b", line):
                                filepath = foldername
                                src = os.path.join(filepath, fnames)
                                dst = os.path.join(tempPath,fnames)
                                copyfile(src, dst)
               
                        

               
            print(" ")
    else:
        print("Invalid Path")




def main():
    print("Director mini antivirus application")

    if(len(argv)!=3):
        print("Insufficient argumnets")
        exit()

    if(argv[1]=="-h"):
        print("this script will tarvel the dircetory and move the suspicious files")
        exit()
    
    if(argv[1]=="-u"):
        print("Usage:Application_name Dircetory_name New_Directory Name")
        exit()

    else:
    
       Directory_Watcher(argv[1],argv[2])
    
    


if __name__=="__main__":
    main()
