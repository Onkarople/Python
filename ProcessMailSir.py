import os 
import time
import psutil
import urllib.request
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



def MailSender(filename):
    try:
        fromaddr="opleonkar@gmail.com"
        toaddr="onkarople@gmail.com"

        msg=MIMEMultipart()

        msg['From']=fromaddr

        msg['To']=toaddr

        body="""
        Hello %s,
        Welcome to Marvellous infosystems.
        please find attched document
        log File is created at:%s

        """%(toaddr,time.strftime("%Y%m%d-%H%M%S"))

        Subject="""
        Marvellous :%s
        """%(time.strftime("%Y%m%d-%H%M%S"))

        msg['Subject']=Subject

        msg.attach(MIMEText(body,'plain'))

        attachment=open(filename,"rb")

        p=MIMEBase('application','octate-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Decomposition',"attachment",filename=filename)

        msg.attach(p)

        s=smtplib.SMTP('smtp.gmail.com',587)

        s.starttls()

        s.login(fromaddr,'aytfdgmzsybdmdka')

        text=msg.as_string()

        s.sendmail(fromaddr,toaddr,text)

        s.quit()

        print("Lof file sucessfully sent through mail")
    
    except Exception as E:
        print("Unbale to sendt mail.",E)
    


def ProcessLog(log_dir='Marvellous'):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    
    separator="-"*80


    timestr = time.strftime("%Y%m%d-%H%M%S")
    log_path=os.path.join(log_dir,"Marvellouslog%s.log"%timestr)
    f=open(log_path,'w')
    f.write(separator+"\n")
    f.write("Marvellous Indosystems "+time.ctime()+"\n")
    f.write(separator+"\n")
    f.write("\n")


    for proc in psutil.process_iter():
        try:
      
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['vms']= proc.memory_full_info().vms/(1024*1024)

            listprocess.append(pinfo)

        except(psutil. NoSuchProcess , psutil.AccessDenied, psutil.ZombieProcess):

            pass
    
    for elem in listprocess:
        f.write("%s\n"%elem)
    
    print("Lof file is succesfully generated at location %s"%(log_path))

    
    MailSender(log_path)
    

def main():
    print("Application Name:"+argv[0])

    if(len(argv)!=2):
        print("Error:Invalid number of arguments")
        exit()
    
    if(argv[1]=='h') or (argv[1]=="-H"):
        print("This script is used log record of running processes")
        exit()
    
    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("usage:ApplicationName time")
        exit()
    
    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Eroor:Invalid datatype of input")

    except Exception as E:
        print("Error :Invalid Input",E)


if __name__ == "__main__":
    main() 

    

    

