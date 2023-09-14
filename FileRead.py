import os

def Read_File(Filename):
    if(os.path.exists(Filename)):

        fd=open(Filename,"r")

        print("Data from the file is")
        print(fd.read())

        fd.close()

    
    else:
        print("File is not exixting")
        return


def main():
    print("Enter the file name ")
    Name = input()

    Read_File(Name)

if __name__ =="__main__":
    main()