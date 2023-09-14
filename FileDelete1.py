import os

def DeleteFile(FileName):
    if(os.path.exists(FileName)):
        size=os.path.getsize(FileName)
        if(size==0):

           os.remove(FileName)
        
        else:
            print("are you sure to delete the file? Y/N")
            option=input()
            if(option=="Y" or option=="y"):
                os.remove(FileName)
            else:
                print("File deletion process stopped.")
                
        
    else:
        print("There no such file")
        return

def main():
    print("Enter the file name to Delete")
    Name = input()

    DeleteFile(Name)

if __name__ =="__main__":
    main()