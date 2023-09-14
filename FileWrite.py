import os

def Write_File(Filename):
    if(os.path.exists(Filename)):
        print("Enter the data that you want to write into file")

        Data=input()

        fd=open(Filename,"a")

        fd.write(Data + " " + "\n")

        fd=open(Filename,"r")

        print(fd.read())

    
    else:
        print("File is not exixting")
        return


def main():
    print("Enter the file name to create")
    Name = input()

    Write_File(Name)

if __name__ =="__main__":
    main()