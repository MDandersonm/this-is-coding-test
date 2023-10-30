#1로 만들기 (4가지 방법을 이용하여 1로 만드는 최소 횟수)

# n=int(input())
n=26
dp=[0]*(n+1)

for i in range(2,n+1):
    dp[i]=dp[i-1]+1

    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
    if i%5==0:
        dp[i]=min(dp[i],dp[i//5]+1)
print(dp[n])
