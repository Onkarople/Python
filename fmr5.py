
from functools import reduce
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

    Arr_Filter=list(filter(lambda no:no%2==0,Data_Input))
    print("Data after filter",Arr_Filter)

    Arr_map=list(map(lambda no:no*2,Arr_Filter))
    print("data after map",Arr_map)

    Ret=reduce(lambda A,B:A+B,Arr_map)
    print("data after reduce",Ret)


if __name__ =="__main__":
    main()