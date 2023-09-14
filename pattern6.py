
def pateern(row,col):
    num=row
    for i in range(1,col+1):
        for j in range(1,num+1):
            print("*",end=" ")
        print()
        num=num-1

    for i in range(1,col+1):
        for j in range(0,i+1):
            print("*",end=" ")
        print()

    
   

            
        
             


def main():
    print("Enter number of rows")
    Row=int(input())

    print("Enter number of coloums")
    Col=int(input())

    pateern(Row,Col)






if __name__ == "__main__":
    main()