import os
import psutil
from  sys import *
import time


def ProcessDsiplay(log_dir="Marvellous"):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    
    separator="-" * 80
    log_path= os.path.join(log_dir,"MarvellousLog%s.log"%(time.strftime("%Y%m%d-%H%M%S")))
    f=open(log_path,'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystems Process Logger : "+time.ctime()+"\n")
    f.write(separator + "\n")


    for proc in psutil.process_iter():

       try:
      
         pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
         vms= proc.memory_full_info().vms/(1024*1024)
         pinfo['vms']=vms
         listprocess.append(pinfo)

       except(psutil. NoSuchProcess , psutil.AccessDenied, psutil.ZombieProcess):

         pass
    
    for element in listprocess:
        f.write("%s\n" % element)


def main():
    print("Marvellos infosystems ")

    print("Application name : "+argv[0])

    if(len(argv)!=2):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"): 
        print("Help: This script is used to perform log record of running processes")
    
    elif(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : ApplicationName AbsolutePath_Of_Directory")
        exit()
    
    try:
        ProcessDsiplay(argv[1])
    except ValueError:
        print("Error:Inavalid Datatype of input")

    except Exception:
        print("Error:Invalid input")
    

if __name__=="__main__":
    main()


