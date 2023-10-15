#재귀함수로 구현한 이진탐색
# def binary_search(array,target,start,end):
#     if start>end:
#         return None
#     mid=(start+end)//2
#     print("mid",mid)
#     if array[mid]==target:
#         return mid
#     elif array[mid]>target:
#         return binary_search(array,target,start,mid-1)
#     elif array[mid]<target:
#         return binary_search(array,target,mid+1,end)
#     return None

def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end )//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        elif array[mid]<target:
            start=mid+1
    return None




n,target= map(int, input().split()) #10,7
array= list(map(int, input().split())) #1 3 5 7 9 11 13 15 17 19
r= binary_search(array,target,0,n-1)
print(r ,"번 인덱스 수 입니다.")