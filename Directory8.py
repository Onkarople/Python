import os 
from sys import *
import hashlib
import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def Mailx(mailid,fname):
    from email import encoders
    mail_content = '''
    Thank You   
    '''
    #The mail addresses and password
    sender_address = 'opleonkar@gmail.com'
    sender_pass = 'zctfdfhevyzaxfgp'
    receiver_address = mailid
    #Setup the MIME

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'
    #The subject line
    #The body and the attachments for the mail

    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = fname
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename

    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


def RemoveDuplicate(dict1):
    results=list(filter(lambda x: len(x)>1,dict1.values()))

    timestr = time.strftime("%Y%m%d-%H%M%S")
    FileName=os.path.join("log%s.log"%(timestr))



    fd=open(FileName,'a')
    icnt=0
    iCount=0
    iDuplicateCount=0
    fd.write("Duplicate files are : ")
    fd.write("\n")

    if len(results)>0:
        print("Duplicate Found")
        for result in results:
            for subresult in result:
                iCount=iCount+1
                icnt+=1
                if icnt>=2:
                    iDuplicateCount=iDuplicateCount+1
                    fd.write(subresult)
                    fd.write("\n")
                    print(subresult)
            icnt=0
                    
    else:
        print("No duplicate files")
    
    return FileName

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

    if(len(argv)!=4):
        print("Insufficient argumnets")
        exit()

    if(argv[1]=="-h"):
        print("this script will tarvel the dircetory and delete duplicate files and write naames of duplicate file name in log file and send lg file to specific mail")
        exit()
    
    if(argv[1]=="-u"):
        print("Usage:Application_name Dircetory_name MailId Number of minutes")
        exit()


    try:
        arr={}
        
        schedule.every(int(argv[3])).minutes.do(lambda:Directory_Cleaner(argv[1]))
        arr=Directory_Cleaner(argv[1])

        schedule.every(int(argv[3])).minutes.do(RemoveDuplicate,arr)
        brr=RemoveDuplicate(arr)
        schedule.every(int(argv[3])).minutes.do(Mailx,argv[2],brr)

        while(True):
            schedule.run_pending()
            return_value=arr
            time.sleep(10)
    

    except Exception as E: 
        print("Exception found",E)
    
    

if __name__=="__main__":
    StartTime=time.time()
    main()
    