#두 배열의 원소 교체
n,k = map(int, input().split())
list1= list(map(int,input().split()))
list2= list(map(int,input().split()))

list1.sort()
list2.sort(reverse=True)


for i in range(k):
    if list1[i] <list2[i]:
        list1[i] =list2[i]
    else:
        break
print(list1)
print(sum(list1))


