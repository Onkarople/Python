
def CheckEven(No):
    if(No%2==0):
        return True
    else:
        return False


def Checkevenx(No):
    return (No%2==0)


CheckEvenxx=lambda No: No%2==0


ret=CheckEvenxx(12)


if(ret==True):
    print("its Even")
else:
    print("its Odd")



