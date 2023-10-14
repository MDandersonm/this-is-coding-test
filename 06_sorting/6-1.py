#선택정렬
array=[7,5,9,0,3,1,6,2,4,8]
#
# for j in range(len(array)):
#     min_value=min(array[j:])
#     i_value= array.index(min_value)
#     array[j], array[i_value] = array[i_value] , array[j] #스와프
#
# print(array)

for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i],array[min_index] = array[min_index],array[i]
print(array)