import os 
from sys import *
import hashlib
import schedule
import time

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()

    buf=afile.read(blocksize)
    while(len(buf)>0):
        hasher.update(buf)
        buf=afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()

def Directory_Watcher(Dir_name):
    print("Inside directory watcher method")
    print("Name of Input Directory : ",Dir_name)

    flag=os.path.isabs(Dir_name)
    if flag==False:
        Dir_name=os.path.abspath(Dir_name)
    
    exists=os.path.isdir(Dir_name)

    dups={}

    if exists:
        for foldername,subfolder,Filenames in os.walk(Dir_name):
           
        
            for fnames in Filenames:
                path=os.path.join(foldername,fnames)
                hashf=hashfile(path)
                if hashf in dups:
                    dups[hashf].append(path)
                else:
                    dups[hashf]=[path]
            
        
        return dups
    
    else:
        print("Invalid path")


def PrintDuplicate(dict1):
    results=list(filter(lambda x: len(x)>1,dict1.values()))

    fd=open("l.txt",'a')


    if len(results)>0:
        print("Duplicate Found")
        icnt=0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    fd.write(subresult)
                    os.remove(subresult)
                    
                else:
                    print("No duplicate files")
                


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


    try:
        arr={}
        arr=Directory_Watcher(argv[1])
        PrintDuplicate(arr)
        
       
    except Exception:
        print("Exception found")
    
    


if __name__=="__main__":
    main()
