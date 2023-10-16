#부품찾기 - 이진탐색
n=int(input())
list1= list(map(int,input().split()))
m=int(input())
list2= list(map(int,input().split()))

list1.sort()
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    elif array[mid]<target:
        return binary_search(array,target,mid+1,end)
    return None


for num in list2:
    if binary_search(list1,num,0,n-1)==None:
        print('no', end=" ")
    else :
        print('yes', end=" ")

