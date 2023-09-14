
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
        for i in range(2,(self.No//2)+1):
            if(self.No%i==0):
                break
        
        if(i==((self.No//2)-1)):
            return True
        else:
            return False

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

    bRet=obj.Chkprimex()
    if bRet==True:
        print("{} Is perfect ".format(A))
    else:
        print(" {} Not perfect".format(A))


if __name__ == "__main__":
    main()