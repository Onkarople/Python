import imp


import os
import multiprocessing
import imp

def Square(No):
    return (No*No)

def main():
    Data=[1,2,3,5,6]

    Result=[]

    pobj=multiprocessing.Pool()

    Result=pobj.map(Square,Data)
    

    print("Result after sqaure operation is:",Result)




if __name__ =="__main__":
    main()