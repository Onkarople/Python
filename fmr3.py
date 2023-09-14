
from functools import reduce


def Checkeven(No):
    return No%2==0


def Incremnt(No):
    return No*2

def Add(A,B):
    return A+B



def AcceptList():
    Data_Input=list()

    print("how many number you want")
    iSize=int(input())

    print("enter Numbers")

    for iCnt in range(0,iSize,1):
        Value=int(input())
        Data_Input.append(Value)

    return Data_Input


def main():
    
    Data_Input=AcceptList() 
    print("List is",Data_Input)

    Arr_Filter=list(filter(Checkeven,Data_Input))
    print("Data after filter",Arr_Filter)

    Arr_map=list(map(Incremnt,Arr_Filter))
    print("data after map",Arr_map)

    Ret=reduce(Add,Arr_map)
    print("data after reduce",Ret)


if __name__ =="__main__":
    main()