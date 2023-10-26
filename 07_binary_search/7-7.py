#부품찾기 - 집합 이용

n=int(input())
list1= set(map(int,input().split()))  #집합으로 찾는게 효율적이다.  집합을 사용하는 경우, 평균적으로 각 요소의 검사가 O(1)이라는 점에서 이점이 있다
m=int(input())
list2= list(map(int,input().split()))

for num in list2:
    if num in list1:
        print("yes" , end=' ')
    else:
        print("no", end =" ")