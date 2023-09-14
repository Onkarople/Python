
class Value:

    def __init__(self,data):
        self.No=data
    
    def SumFactors(self):
        sum=0
        for i in range(1,(self.No//2)+1):
            if(self.No %i==0):
                sum=sum+i
        
        return sum
    
    def Chkperfect(self):
        Ans=self.SumFactors()

        if(Ans==self.No):
            return True
        else:
            return False

    def Chkprime(self):
        Flag=True
        for i in range((self.No//2)+1,2,-1):
            if(self.No%i==0):
                Flag=False
                break
        
        return Flag
    def Chkprimex(self):
        Ans=self.SumFactors()

        if(Ans>0):
            return True
        else:
            return False



def main():
    print("Enter number")
    A=int(input())

    obj=Value(A)

    oytput=obj.SumFactors()
    print("Sum is",oytput)

    bRet=obj.Chkprime()
    if bRet==True:
        print("{} Is prime ".format(A))
    else:
        print(" {} Not prime".format(A))


if __name__ == "__main__":
    main()