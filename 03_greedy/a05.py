#05 볼링공 고르기 - 서로다른무게의 볼링공2개 고르기
n,m= map(int,input().split())
array =list(map(int,input().split()))
#
# cnt=0;
# for i in range(len(array)):
#     for j in range(i+1, len(array)):
#         if array[i] !=array[j]:
#             cnt+=1
# print(cnt)

#answer

list= [0]*11 # 볼링공 무게
print(list)
for x in array:
    #각 무게에 해당하는 볼링공 개수 카운트
    list[x] +=1
print(list)

result=0
for i in range(1,m+1):
    n=n-list[i]
    result += list[i]*n
print(result)