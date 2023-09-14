
def pateern(row,col):
    for i in range(1,col+1):
        for j in range(1,i+1):
            if i==j:
                print("1",end=" ")
            elif i%2!=0 and ((j==1) or (j%2!=0)):
                print("1",end=" ")
            elif ((i%2)==0) and ((j%2)==0):
                print("1",end=" ")
            else:
                print("0",end=" ")
        print()            
            


def main():
    print("Enter number of rows")
    Row=int(input())

    print("Enter number of coloums")
    Col=int(input())

    pateern(Row,Col)






if __name__ == "__main__":
    main()