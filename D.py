


def fun(no1):
    s=str(no1)
    d=len(s)
    no3=d
    sum=0
    i=0
    temp=no1
    

    while(no1!=0):
        mult=1
        no2=int(s[i])

        mult=no2**no3

    
        sum=sum+mult
        i=i+1
        no1=no1//10
    
    
    no1=temp

    
    if(no1 == sum):
        return True
    else:
        return False




def main():
    print("Enter number")
    x=int(input())
    y=fun(x)
    print(y)
    if(y==True):
        print("amstrong")
    else:
        print("no")


main()
