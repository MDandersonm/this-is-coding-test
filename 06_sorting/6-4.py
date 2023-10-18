#퀵정렬

array =[5,7,9,0,3,1,6,2,4,8]

# 중도 포기
# def quick_sort(array,start,end):
#     print("새로운 quick sort, start:",start,"end:",end) #2,4
#     pivot=array[start] #0
#     start_index=start
#     end_index=end
#     if start>=end:
#         return
#     n=0
#     while 1:
#         flg1=False
#         flg2=False
#         # print("true문")
#         for i in range(start+1, end_index+1): #3 ,4
#             if pivot<array[i]:#2<4
#                 start=i #start=3
#                 # print("start",start)
#                 flg1=True
#                 break
#         for j in range(end, start_index, -1):# 4,3
#             if pivot>array[j]:
#                 end=j-1
#                 # print("end",end)
#                 flg2=True
#                 break
#         print("i",i, "j",j)
#         if i<j and flg1 and flg2:
#             array[i],array[j]= array[j],array[i]
#             print("i<j",array)
#         elif i>=j and flg1 and flg2:
#             array[start_index]=array[j]
#             array[j]=pivot
#             print("i>=j",array)
#             break
#         else:
#             break
#     quick_sort(array,start_index,j-1)
#     quick_sort(array,j+1,end_index)
#
#
#
# quick_sort(array,0,len(array)-1)
# print(array)
def quick_sort(array,start,end):#3,4
    print("start",start,"end",end)
    if start>=end:
        return
    pivot=start
    left=start+1#4
    right=end#4
    while left<=right: #4=4 #두장남을때는 left=right일것.
        while left<=end and array[left]<array[pivot]: # 4=4 left를 옆으로 한칸씩 옮길때 끄
            left+=1 #left=5
        while start<right and array[pivot]<array[right]:  #3<4  4<=3
            right-=1 #right=4
        print("left",left,'right',right)

        if left>right:#역전되면 피벗값 이동
            array[start],array[right]  = array[right],array[pivot] #
        else:#left<=right
            array[left],array[right]= array[right],array[left]
        print("array", array)

    quick_sort(array,start, right-1)
    quick_sort(array, right+1,end)
quick_sort(array,0,len(array)-1)
print(array)

