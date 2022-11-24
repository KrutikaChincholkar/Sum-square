data=input("data:")
list1=data.split(",")
size1=len(list1)
for i in range(size1):
    list1[i]=int(list1[i])
sum1=sum(list1)
print(sum1)

for i in range(size1):
    list1[i]=list1[i]*list1[i]
print(list1)
sum2=sum(list1)
print(sum2)
