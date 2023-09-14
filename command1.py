from sys import *

def main():
    print("total number of arguments are:",len(argv))

    print("Name of application :",argv[0])

    print("First argumnet",argv[1])
    print("second argumnet",argv[2])
    print("Third argument",argv[3])


if __name__ =="__main__":
    main()


#           0       1   2    3    
#python command1.py 12 hello 22