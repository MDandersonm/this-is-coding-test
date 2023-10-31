#개미전사 이웃하지 않은 값들의 최댓값
n =int(input())
list1= list(map(int,input().split()))

dp=[0]*(n+1)
dp[0]=list1[0]
dp[1]=max(list1[0],list1[1])
for i in range(2,n):
    dp[i]=max(dp[i-1],list1[i]+dp[i-2])
print(dp[n-1])