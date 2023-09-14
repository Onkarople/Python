
def Add(A,B):
    ANs=A+B
    return ANs

def Sub(A,B):
    ANs=A-B
    return ANs

def main():
    print("Enter first number")
    No1=int(input())

    print("Enter second number")
    No2=int(input())

    Ret=Add(No1,No2)

    print("Addition is:",Ret)

    Ret=Sub(No1,No2)
    print("subsrtaion is:",Ret)





if __name__ == "__main__":
    main()