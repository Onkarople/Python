import psutil
from sys import *
import os
from signal import *
import subprocess
import Multiprocessing

def ProcessDisplay(PName):
   listprocess = []
  

   for proc in psutil.process_iter():

    try:
      
       pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
       if PName in pinfo['name']:
            listprocess.append(pinfo)

    except(psutil. NoSuchProcess , psutil.AccessDenied, psutil.ZombieProcess):

       pass

  

   if len(listprocess)>0:
      for elem in listprocess:
            processId=elem['pid']
            processName=elem['name']
            os.kill(processId,SIGTERM)
   

   print("Process Killed")

          
            

   

def main():
  print("Marvellous Infosystems : Python Automation & Machine Learning")

  print("Process Monitor")

  if(len(argv)!=2):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

  if(argv[1]=="-h") or (argv[1]=="-H"): 
        print("Help: This script is used to perform __________")
     
  elif(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Provide ______ number of argumnets as")
        print("First Argument as _____")
        print("Second Argument as :_____")
        exit()

  else:
     ProcessDisplay(argv[1])
    

 

if __name__ =="__main__":
    main()