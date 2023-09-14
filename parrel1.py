import os
import multiprocessing
import imp

def Square(No):
    print("PID of worker process is {} for the input {} ".format(os.getpid(),No))
    return (No*No)

def main():
    print("Process ID of our Application Is:",os.getpid())

    Data=[1,2,3,5,6]

    Result=[]

    pobj=multiprocessing.Pool()

    Result=pobj.map(Square,Data)
    

    print("Result after sqaure operation is:",Result)




if __name__ =="__main__":
    main()