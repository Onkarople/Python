
Checkeven=lambda No: No%2==0

Doubles =lambda No: No*2

Add=lambda A,B : A+B

def filterx(Helper_Function,Data):
    Result=[]
    for No in Data:
        if(Helper_Function(No)==True):
            Result.append(No)
    return Result


def mapx(Helper_Function,Data):
    Result=[]
    for No in Data:
        value=Helper_Function(No)
        Result.append(value)
    return Result


def reducex(Helper_Function,Data):
    sum=0
    for no in Data:
        sum=Helper_Function(no,sum)
    return sum



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



    Data_Filter=filterx(Checkeven,Data_Input)
    print("Data after filter",Data_Filter)



    Data_map=mapx(Doubles,Data_Filter)
    print("data after map",Data_map)


    Output=reducex(Add,Data_map)
    print("data after reduce",Output)





if __name__ =="__main__":
    main()