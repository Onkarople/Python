
class Numbers:

    def __init__(self):
        self.size=0
        self.Arr=list()
       
    

    def Add(self):
        sum=0
        for No in self.Arr:
            sum=sum+No
        
        return sum
    
    def Accept(self):
        print("Enter how many elements you want")
        self.size=int(input())

        No=0

        print("Enter elements")
        for i in range(0,self.size):
            No=int(input())
            self.Arr.append(No)
    
    def Display(self):
        print("elements from list are:")
        for i in range(0,self.size):
            print(self.Arr[i])



              
def main():
    obj=Numbers()
    
    obj.Accept()
    obj.Display()
    Output=obj.Add()
    print("Ans is",Output)


if __name__ == "__main__":
    main()