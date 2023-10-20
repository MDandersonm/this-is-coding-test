#계수정렬
array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

list1= [0]*(max(array)+1)

for i in array:
    list1[i]+=1

print(list1)
for i in range(len(list1)):
    for k in range(list1[i]):
        print(i, end=' ')

