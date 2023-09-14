
#positional arguments/keyword arguments
def Add1(No1,No2):
    print("value of No1:",No1)
    print("value of No2:",No2)

    return No1+No2

def Sub(No1,No2):
    print("value of No1:",No1)
    print("value of No2:",No2)

    return No1-No2



def main():
    Ans=0
    Ans=Add1(10,11)
    print("Addition is:",Ans)

    Ans=Sub(No2=10,No1=11)
    print("substration  is:",Ans)

    Ans=Sub(No1=10,No2=11)
    print("substration  is:",Ans)





if __name__ == "__main__":
    main()