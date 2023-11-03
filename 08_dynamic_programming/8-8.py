#효율적인 화폐 구성

n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp 테이블 초기화. 불가능한 값으로 m+1을 넣어준다.
# dp[i]는 i원을 만들기 위한 최소한의 화폐 개수를 의미한다.
dp = [m + 1] * (m + 1)
dp[0] = 0 #화폐를 하나도 사용하지 않았을때 만들수 있는 값으로 0 설정

# 예를 들어, 화폐가 2원이고 현재 j가 5라고 가정해 봅시다. 그럼 j - coin은 5 - 2 = 3이 되므로, 3원을 만들 수 있는지 확인하는 것입니다. 만약 3원을 만들 수 있다면, dp[3]의 값은 m + 1보다 작게 되어 있을 것입니다.
#따라서, if dp[j - coin] != m + 1   조건문은 "(j-coin)원을 만들 수 있다면, j원도 해당 화폐를 하나 더 추가해서 만들 수 있다"는 로직을 수행하기 위한 것입니다.
for coin in coins:
    for j in range(coin, m + 1):
        if dp[j - coin] != m + 1:  # (j-coin)원을 만들 수 있다면
            dp[j] = min(dp[j], dp[j - coin] + 1)
            print("j",j,"dp[j]",dp[j])

# m원을 만들 수 없는 경우
if dp[m] == m + 1:
    print(-1)
else:
    print(dp[m])
