import os 
from sys import *
from shutil import copyfile
import fnmatch

def Directory_Watcher(Dir_name,Ext):

    os.mkdir("Cp")
    new_path="Cp"

    print("Inside directory watcher method")
    print("Name of Input Directory : ",Dir_name)

    flag=os.path.isabs(Dir_name)
    if flag==False:
        Dir_name=os.path.abspath(Dir_name)
    
    exists=os.path.isdir(Dir_name)

    if exists:




        for foldername,subfolder,Filenames in os.walk(Dir_name):
            print("Folder name is : "+foldername)
            for subf in subfolder:
                print("subfolder name of : "+foldername+" is :"+subf)
        
            for fnames in Filenames:
                s=fnames.split('.')

                if s[1]==Ext[1:]:
                 filepath = foldername
                src = os.path.join(filepath, fnames)
                dst = os.path.join(new_path,fnames)
                copyfile(src, dst)
            
            
        
        print(" ")
    else:
        print("Inavlid path")




def main():
    print("Directory watcher application")

    if(len(argv)!=3):
        print("Insufficient argumnets")
        exit()

    if(argv[1]=="-h"):
        print("this script will tarvel the dircetory and dispaly the anem of all entries")
        exit()
    
    if(argv[1]=="-u"):
        print("Usage:Application_name Dircetory_name")
        exit()


    
    Directory_Watcher(argv[1],argv[2])
    
    


if __name__=="__main__":
    main()
