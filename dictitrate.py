

batches={"PPA":18000,"LB":16700,"python":16500,"angular":1500}

print("data of dictnoary:",batches)


print("data traversal using for loop")
for x in batches:
    print(x)



print("data traversal using for loop")
for x in batches:
    print(x," : ",batches[x])




print("data traversal using for loop")
for x in batches:
    print(x,batches.get(x))



keyBatches=batches.keys()


print(keyBatches)
print(type(keyBatches))


valueBatches=batches.values()

print(valueBatches)
print(type(valueBatches))


   
    