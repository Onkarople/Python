
def Square(No):
    return (No*No)

def main():
    Data=[1,2,3,5,6]

    Result=[]

    for Value in Data:
        Result.append(Square(Value))
    

    print("Result after sqaure operation is:",Result)




if __name__ =="__main__":
    main()