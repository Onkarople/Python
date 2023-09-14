#PPA ani LB chi punyai
print("Application to demonstrate Industrial programming")

def Addition(value1,value2):
    Ans = value1 + value2
    return Ans


def main():
    print("Enter first number : ")
    no1=input()
    print("Enter second number:")
    no2=input()

    sum = Addition(int(no1),int(no2))
   

    print("Addition is:",sum)
 
if __name__ == "__main__":

    main()