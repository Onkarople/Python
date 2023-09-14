
# data:Hetrogenous
#Orderd:yes
#Indexed:yes
#Mutable:yes
#allows duplicate




Data=[11,21,51,101]


print("output using for loop")
for No in Data:
    print(No,end=" ")
print("______________________")


print("output using for loop with index")
for i in range(0,len(Data)):
    print(Data[i],end=" ")
print("___________________________")


print("output using while with index")
i=0
while(i<len(Data)):
    print("Index:",i," data is",Data[i])
    i+=1
print("_______________________________")





