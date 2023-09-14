#display factors

def Fact(No):
    if(No<0):
        return
        
    print("factors are")
    i=1
    while(i<=No//2):
        if(No%i==0):
            print(i)
        i=i+1
         


def main():
    print("Enter number")
    No=int(input())
    Fact(No)


if __name__ == "__main__":
    main()