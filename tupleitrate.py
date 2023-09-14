
# data:Hetrogenous
#Orderd:yes
#Indexed:yes
#Mutable:no
#allows duplicate




Data=(11,21,51,101)


print("\n_______________________")


print("output using for loop")
for No in Data:
    print(No,end=" ")
print("\n______________________")


print("\n output using for loop with index")
for i in range(0,len(Data)):
    print(Data[i],end=" ")
print("\n___________________________")


print("output using while with index")
i=0
while(i<len(Data)):
    print("Index:",i," data is",Data[i])
    i+=1
print("\n_______________________________")





