import os 
from sys import *


def Directory_Watcher(Dir_name):
    print("Inside directory watcher method")
    print("Name of Input Directory : ",Dir_name)

    flag=os.path.isabs(Dir_name)
    if flag==False:
        Dir_name=os.path.abspath(Dir_name)
    
    exists=os.path.isdir(Dir_name)
    icnt=0

    if exists:


        for foldername,subfolder,Filenames in os.walk(Dir_name):
            print("Folder name is : "+foldername)
            for subf in subfolder:
                print("subfolder name of : "+foldername+" is :"+subf)
        
            for fnames in Filenames:
                print("File Inside folder : " +foldername+" is "+fnames)
                icnt=icnt+1
        
            print(" ")
        print(icnt)
    else:
        print("Invalid Path")




def main():
    print("Directory watcher application")

    if(len(argv)!=2):
        print("Insufficient argumnets")
        exit()

    if(argv[1]=="-h"):
        print("this script will tarvel the dircetory and dispaly the anem of all entries")
        exit()
    
    if(argv[1]=="-u"):
        print("Usage:Application_name Dircetory_name")
        exit()


    
    Directory_Watcher(argv[1])
    
    


if __name__=="__main__":
    main()
