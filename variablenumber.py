#varible number of arguments

from optparse import Values


def Add(*Values):
    print(type(Values))
    print("Number of arguments are",len(Values))
    sum=0

    for no in Values:
        sum=sum+no
    

    return sum

def Addx(*Values):
    sum=0

    for i in range(0,len(Values),1):

        sum=sum+Values[i]

    return sum

 

def main():
    Ans=0
    Ans=Add(1,7,9,6,5,4)
    print("Addition is",Ans)

    Ans=Addx(10,11)
    print("Addition is",Ans)



if __name__ =="__main__":
    main()