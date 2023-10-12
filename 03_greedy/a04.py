#만들수 없는 금액 - 5가지 동전으로 만들수 없는 최소값
n=int(input())
array = list(map(int, input().split()));
#
# result=[]
# from itertools import combinations
# for i in range(1,n+1):
#     result += list(combinations(array, i))  # 2개를 뽑는 모든 조합
#
# print(result)
# result2=[]
# for tuple in result:
#     sum=0;
#     for x in tuple:
#         sum+=x
#     result2.append(sum)
# result2.sort()
# print(result2)
# for idx,i in enumerate(set(result2)):
#     if idx+1 != i:
#         print(idx+1)
#         break

#answer
array.sort()
target=1
for x in array:
    if target<x:
        break
    target+=x
print(target)