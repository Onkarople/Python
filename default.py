
def Area(Radius,PI=3.14):
    Result=PI*Radius*Radius
    return Result

def main():
    Rvalue=10.5
    PIvalue=3.14

    Ans=Area(Rvalue,PIvalue)  #Area(10.5,3.13) positonal
    print("area of circul is:",Ans)

    Ans=Area(PI=PIvalue,Radius=Rvalue)   #keyword
    print("area of circul is:",Ans)

    Ans=Area(10.5)  #Area(10.5)     #positional deafult
    print("area of circul is:",Ans)

    Ans=Area(Radius=10.5)  #Area(Radius=10.5)  keyword default
    print("area of circul is:",Ans)

    Ans=Area(PI=7.10,Radius=10.5)  #keyword  
    print("area of circul is:",Ans)

    Ans=Area(Rvalue,PI=PIvalue)  #Area(10.5)  #positional ani keyword
    print("area of circul is:",Ans)

    




if __name__ =="__main__":
    main()