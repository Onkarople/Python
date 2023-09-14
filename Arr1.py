
def sum(Arr,size):
    Ret=0

    for i in range(0,size):
        Ret=Ret+Arr[i]
    
    return Ret




def main():
    Arr=list()

    print("Enter how many elements you want")
    size=int(input())

    print("Enter elements")

    for i in range(0,size):
        no=int(input())
        Arr.append(no)
    
    Ans=sum(Arr,size)

    print("Sum is:",Ans)
    

if __name__ == "__main__":
    main()