#PPA ani LB chi punyai
print("Application to demonstrate Industrial programming")

import Marvellousmodule

def main():
    print("value of __name__  from main is:",__name__)
    print("Enter first number : ")
    no1=input()
    print("Enter second number:")
    no2=input()

    sum = Marvellousmodule.Addition(int(no1),int(no2))
   

    print("Addition is:",sum)
 
if __name__ == "__main__":
    main()