n=4
m=3
array= [[0]*m for _ in range(n)] #4행3열
print(array)

print([2]*5)

array[1][1]=5
print(array)

#공백을 기준으로 구분된 데이터를 받을 때
# list1=list(map(int,input().split()))
# print(list1)
# a,b,c= map(int, input().split())
# print(a,b,c)

#빠르게 입력받기
# import sys
# data=sys.stdin.readline().rstrip()
# print(data)

#f-string
answer=7
print(f"정답은 {answer}입니다")

#lambda
print( (lambda a,b:a+b)(3,4))

#점수순 정렬
array2= [('홍길동',50),('이순신',32), ('아무개',75)]
print(sorted(array2, key=lambda x:x[1]))

#리스트 각각 원소 합
list1= [1,2,3,4,5]
list2= [6,7,8,9,10]
result= map(lambda a,b:a+b,list1,list2)
print(list(result))

#itertools
#순열
from itertools import permutations
data= ['a','b','c']
result= list( permutations(data,3)) #순열
print(result)

#조합
from itertools import combinations
result2= list( combinations(data,2)) #2개를 뽑는 모든 조합
print(result2)

#중복순열
from itertools import product
result3= list(product(data,repeat=2))
print(result3)

#중복조합
from itertools import combinations_with_replacement
result4= list(combinations_with_replacement(data,2))
print(result4)

#Counter 등장횟수세기
from collections import Counter
counter= Counter(['red','blue','red','green'])
print(counter['blue'])
print(counter['red'])
print(dict(counter))

import math
#최대 공약수 gcd()
print( math.gcd(21,14))

#최소 공배수
def lcm(a,b):
    return a*b // math.gcd(a,b)
print(lcm(21,14)) #최소공배수

 