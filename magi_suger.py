dict={"magi":10,"suger":100,"oil":50,"solt":30}
quantity=input("enter the key ")
quantity2=input("enter the key ")
# dict={"magi":10,"suger":100,"oil":50,"solt":30}
for i in dict.keys():
    if quantity==i:
        key1=i
for i in dict.keys():
    if quantity2==i:
        key2=i
sum=dict[key1]+dict[key2]
print(sum)
    
    