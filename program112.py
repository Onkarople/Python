import os 
from sys import *
import hashlib


def Directory_Watcher(Dir_name):
    print("Inside directory watcher method")
    print("Name of Input Directory : ",Dir_name)
    fcreate=open("Log.txt","a")

    

    for foldername,subfolder,Filenames in os.walk(Dir_name):
        
        for fnames in Filenames:
          with open(os.path.join(foldername,fnames,),'rb') as Fd:
             data=Fd.read()
             md5ans=hashlib.md5(data).hexdigest()
             fcreate.write(fnames)
             fcreate.write(" ")
             fcreate.write(md5ans)
             fcreate.write("\n")
           

        print(" ")




def main():
    print("Directory watcher application")

    if(len(argv)!=2):
        print("Insufficient argumnets")
        exit()

    if(argv[1]=="-h"):
        print("this script will tarvel the dircetory and dispaly the checksum")
        exit()
    
    if(argv[1]=="-u"):
        print("Usage:Application_name Dircetory_name")
        exit()


    
    Directory_Watcher(argv[1])
    
    


if __name__=="__main__":
    main()
