
#Normal functions/named functions
#def Function_NAme(Function_parameters):
#    function_Body

def Add(no1,no2):
    return no1+no2


#lambda functions/Unnamed functions
#lambda paramenetrs:body

addFunction=lambda A,B : A+B


Ans1=Add(10,11)

Ans2=addFunction(10,11)

print("Addi using normal function is:",Ans1)
print("Add using lambda function:",Ans2)

print(type(addFunction))