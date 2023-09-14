#display factors

def Fact(No):
    print("factors are")
    for i in range(1,(No//2)+1):
        if(No%i==0):
            print(i)


def main():
    print("Enter number")
    No=int(input())
    Fact(No)


if __name__ == "__main__":
    main()