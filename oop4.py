
class Numbers:

    def __init__(self):
        self.size=0
        self.Arr=list()
        self.Accept()
        self.Display()

    def Add(self):
        sum=0
        for No in self.Arr:
            sum=sum+No
        
        return sum

    def Average(self):
        sum=0
        for No in self.Arr:
            sum=sum+No
        
        return (sum/self.size)

    def Max(self):
        max=self.Arr[0]
        for No in self.Arr:
            if max<No:
                max=No
        
        return max
    
    def Min(self):
        min=self.Arr[0]
        for No in self.Arr:
            if min>No:
                min=No
        
        return min
    
    def Count(self,No1):
        iCnt=0
        for No in self.Arr:
            if No1==No:
                iCnt=iCnt+1
        
        return iCnt

    
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
    
    Output=obj.Add()
    print("Ans is",Output)

    Output=obj.Average()
    print("Average is",Output)

    Max=obj.Max()
    print("Maximum is",Max)

    Min=obj.Min()
    print("Minimum is",Min)

    print("Enetr one numebr")
    No1=int(input())

    count=obj.Count(No1)
    print("Cont is",count)

if __name__ == "__main__":
    main()