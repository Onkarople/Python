#class=Characterstics + Behaviours
#class=data+Function
#accept 2 numbers and perform addition and substration of it
#first question-tula kay karyach
#second question-tya sathi tula kay lagnar


class Arthematic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B


    def Add(self):
        Ans=self.No1+self.No2
        return Ans
    
    def Sub(self):
        Ans=self.No1-self.No2
        return Ans
    

def main():
    print("Enter first number")
    No1=int(input())

    print("Enter second number")
    No2=int(input())

    obj=Arthematic(No1,No2)
    Ans=obj.Add()

    print("Addition is",Ans)

    obj=Arthematic(No1,No2)
    Ans=obj.Sub()

    print("substration is",Ans)




if __name__=="__main__":
    main()