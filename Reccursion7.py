
def Display(No):
    sum=0
    while(No>0):
         sum=sum+No
         No=No-1

    return sum

def main():
    No=int(input("Enter Number : "))
    Ret=Display(No)
    print("Addition is :",Ret)

if __name__=="__main__":
    main()