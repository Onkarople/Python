
class Arthematic:
    def __init__(self,A,B):
        print("Inside init method")
        self.No1=A
        self.No2=B
    

    def Addition(self):
        Ans=self.No1+self.No2
        return Ans
    
    def Substration(self):
        Ans=self.No1-self.No2
        return Ans








def main():
    print("inside main method")
    obj=Arthematic(11,10)

    output=obj.Addition()
    print("Addition is:",output)

    output=obj.Substration()
    print("substrion  is:",output)


    objx=Arthematic(21,20)
    output=objx.Addition()
    print("Addition is:",output)

    output=objx.Substration()
    print("substrion  is:",output)







if __name__ == "__main__":
    print("Inside starter")
    main()