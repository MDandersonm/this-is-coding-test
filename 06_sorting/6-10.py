#위에서 아래로
n=int(input())#3
list1=[] #15,27,12
for _ in range(n):
    list1.append(int(input()))

list1.sort(reverse=True)
for x in list1:
    print(x, end=" ")
