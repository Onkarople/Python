
def Checkeven(No):
    return (No%2==0)


def Increment(No):
    return No+2


def Filterx(Arr,Function_Name):
    Result=[]
    for no in Arr:
        if(Function_Name(no)):
            Result.append(no)
        
    return Result

def mapX(Arr,Function_Name):
    Result=[]

    for no in Arr:
        value=Function_Name(no)
        Result.append(value)
    return Result


def reducex(Arr):
    sum=0
    for no in Arr:
        sum=sum+no
    

    return sum

   
def main():
   
    Data=[12,3,1,6,2,5,8]

    print("orignal data",Data)

    data_Filter=list(Filterx(Data,Checkeven))

    print("Data after filter:",data_Filter)

    Data_map=list(mapX(data_Filter,Increment))

    print("Data after map",Data_map)


    ret=reducex(Data_map)

    print("Data after map:",ret)




if __name__=="__main__":
    main()