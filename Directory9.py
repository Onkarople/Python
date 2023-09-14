import os 
from sys import *
import hashlib
import schedule
import time

def RemoveDuplicate(dict1):
    results=list(filter(lambda x: len(x)>1,dict1.values()))

    timestr = time.strftime("%Y%m%d-%H%M%S")
    FileName=os.path.join("Log%s.log"%(timestr))



    fd=open(FileName,'a')
    icnt=0
    fd.write("Duplicate files are : ")
    fd.write("\n")

    if len(results)>0:
        print("Duplicate Found")
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    fd.write(subresult)
                    fd.write("\n")
                    print(subresult)
            icnt=0
                    
    else:
        print("No duplicate files")

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()

    buf=afile.read(blocksize)
    while(len(buf)>0):
        hasher.update(buf)
        buf=afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()

def Directory_Cleaner(Dir_name):
    print("Inside directory cleaner method")
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


                


def main():
    print("Directory Cleaner application")

    if(len(argv)!=2):
        print("Insufficient argumnets")
        exit()

    if(argv[1]=="-h"):
        print("this script will tarvel the dircetory and delete duplicate files and write naames of duplicate file name sin log file ")
        exit()
    
    if(argv[1]=="-u"):
        print("Usage:Application_name Dircetory_name")
        exit()


    try:
        arr={}
        
        schedule.every(1).minutes.do(lambda:Directory_Cleaner(argv[1]))
        arr=Directory_Cleaner(argv[1])

        schedule.every(1).minutes.do(RemoveDuplicate,arr)

        while(True):
            schedule.run_pending()
            return_value=arr
            time.sleep(10)
    

    except Exception as E: 
        print("Exception found",E)
    
    

if __name__=="__main__":
    main()
    