
def pateern(row,col):
    for i in range(1,col+1):
        for j in range(1,row+1):
            if (i+j)==(row+1):
                print("*",end=" ")
            else:
                print("@",end=" ")
        print()
             


def main():
    print("Enter number of rows")
    Row=int(input())

    print("Enter number of coloums")
    Col=int(input())

    pateern(Row,Col)






if __name__ == "__main__":
    main()