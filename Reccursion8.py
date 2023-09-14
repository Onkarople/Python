
def Display(No):
    if(No<=0):
        return 0
    else:
        return(No+Display(No-1))
       


def main():
    No=int(input("Enter Number : "))
    Ret=Display(No)
    print("Addition is :",Ret)

if __name__=="__main__":
    main()