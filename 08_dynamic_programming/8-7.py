# 바닥공사 (타일채우는 방법 가지수)

n=int(input())

dp=[0]*(n+1)

dp[1]=1
dp[2]=3
for i in range(3,n+1):
    dp[i]=(dp[i-1]+dp[i-2]*2) %796796
print(dp[n])
