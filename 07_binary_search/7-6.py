#부품탐색 -계수정렬
n=int(input()) # 1,000,000
array=[0]*1000001  # 1,000,000으로하면  index가 부터 999999까지 있을것.
for i in map(int,input().split()): #2~ 1,000,000
    array[i]=1

m=int(input())
list2= list(map(int,input().split()))

for num in list2:
    if array[num]==1:
        print("yes" ,end=' ')
    else:
        print("no", end=" ")
