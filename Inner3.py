

def Add(A,B):
    return A+B

def sub(A,B):
    return A-B


def Calculater(Target,Value1,Value2):
    return Target(Value1,Value2)


ret=Calculater(Target=Add,Value1=10,Value2=11)
print("Addition is:",ret)

ret=Calculater(Target = sub , Value1=10 , Value2=11)
print("sub is:",ret)
