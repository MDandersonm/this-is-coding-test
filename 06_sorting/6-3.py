#삽입정렬
array=[7,5,9,0,3,1,6,2,4,8]

# for i in range(1,len(array)):
#     print("i",i)
#     temp=array[i]
#     for j in range(i-1,-1,-1):
#         print("j",j)
#         if array[j] > temp: #array[0]>array[1]
#             array[j+1]=array[j] #array[1]=array[0]
#             if j==0:
#                 array[j]=temp
#         else:
#             array[j+1]=temp
#             print("array:",array)
#             break
# print(array)

#answer  temp 를 사용안하니까 메모리사용측면에서 유리
for i in range(1,len(array)):
    for j in range(i-1,-1,-1):
        if array[j] > array[j+1]:
            array[j],array[j+1]= array[j+1],array[j] #스와프
        else:
            print("array:",array)
            break
print(array)