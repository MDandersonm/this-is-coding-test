#숫자카드게임 - 각 행에서 가장 숫자가 낮은카드 중 그 중 젤 큰 수
n,m= map(int, input().split()) #행, 열

#my sol
# list1=[]
# for _ in range(n): #행
#     list1.append(list(map(int, input().split())))
#
# print(list1)
# ans=0
# for l in list1:
#     if min(l)>ans:
#         ans=min(l)
# print(ans)

#answer
result=0
for _ in range(n): #행
    data=list(map(int, input().split()))
    result=max(result,min(data))
print(result)
