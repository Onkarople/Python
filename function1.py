#Function which accepts nothing and return nothing
def Demo1():
    print("inside demo1")

#Function which accepts one parameter and return nothing
def Demo2(No):
    print("inside demo2 with one argument")
    print("value of No is:",No)


#Function which accepts one parameter and return one parameter
def Demo3(No):
    print("Inside demo3 with one arguments",No)
    return No+2


#Function which accepts two paramter and return one parameter
def Demo4(No1,No2):
    print("inside demo4")
    Add=No1+No2
    return Add


#Function which accepts two paramter and return two parameter
def Demo5(No1,No2):
    print("inside demo5")
    Add=No1+No2
    sub=No1-No2
    return Add,sub


#main function to call other function
def main():
    Demo1()

    Demo2("Hello")

    Ans=Demo3(10)
    print("Returnted value of demo3 is:",Ans)

    Ans=Demo4(10,11)
    print("return value is:",Ans)

    Ans1,Ans2=Demo5(11,10)
    print("first return value ",Ans1)
    print("Second return value",Ans2)





if __name__ == "__main__":
    main()