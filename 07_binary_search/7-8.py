#떡볶이 떡 만들기 - 특정 최소 길이를 만족하는 자르기 최대 높이
n,m= map(int,input().split())
array = list(map(int,input().split()))

# 선형탐색-매우비효율적.
# for k in range(max(array)-1,0,-1):
#     list2 = [num - k if num - k >= 0 else 0 for num in array]
#     print(list2)
#     if sum(list2)==m:
#         print(k)
#         break
#

#answer 이진탐색
result=0
def binary_search(array,target,start,end):
    global result
    while start<=end:
        mid=(start+end )//2
        total=0
        for x in array:
            if x-mid>0:
                total+= (x-mid)

        if total>=target:#떡의양 많음
            start = mid + 1
            result = mid
        elif total<target:#떡의 양 부족
            end = mid - 1
    return None

binary_search(array,6,0, max(array))
print(result)