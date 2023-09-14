print("demonstration of set ")


#data:Hetrogenous
#Orderd:No
#Indexed:No
#Mutable:yes
#Not allows duplicate


data={11,21,51,101,21,11,201}  #not allowed duplicates

data1={11,90.30,True,"hello"} #hetrogenous



print("data is hetrogenous:",data1)
print("length of data",len(data))
print("data is unorderd",data)
#print("Data at index 2",data[2])
print("data with  no duplicates elemnts:",data)


print("set is mutable")

#insert elelment in set 

data.add(211)

print("data after insertion is",data)


#remove element
data.remove(201)

print("data after removal",data)

data.discard(202)
print("data after discard",data)

