
from functools import reduce
Checkeven=lambda No: No%2==0

Doubles =lambda No: No*2

Add=lambda A,B : A+B

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

    Data_Filter=list(filter(Checkeven,Data_Input))
    print("Data after filter",Data_Filter)

    Data_map=list(map(Doubles,Data_Filter))
    print("data after map",Data_map)

    Output=reduce(Add,Data_map)
    print("data after reduce",Output)


if __name__ =="__main__":
    main()