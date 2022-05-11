name=input("Enter name :")
i=0
count=0
while i<len(name):
    k="a,e,i,o,u"
    if name[i] in k:
        count+=1
    i=i+1
print(count)



