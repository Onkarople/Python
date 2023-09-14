

def Substration(No1,No2):  #200
    Ans=0
    Ans=No1-No2
    return Ans


def Decorated_Function(Function_Name):  #Function_Name=200
    def Inner(A,B):  #300 
        if(A<B):
            A,B=B,A
        output=Function_Name(A,B)  #200(12,8)
    
        return output  
    
    return Inner  #return 300


def main():   #100
    Value1=int(input("Enter first Number:"))  #8
    Value2=int(input("Enter second Number:")) #12

    New_Function=Decorated_Function(Substration) #Decorated_Function(200)
    Ret=New_Function(Value1,Value2)  #ret=300(8,12)
    print("Substratuion is :",Ret)  

if __name__ =="__main__":
    main()  #call 100()