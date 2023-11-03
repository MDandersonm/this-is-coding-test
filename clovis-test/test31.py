MOD = 1_000_000_007

memo = {}

def find_ways(pos, k, last_jump):
    if k == 0:
        return 1 if pos == 0 else 0
    if (pos, k, last_jump) in memo:
        return memo[(pos, k, last_jump)]

    ways = 0
    for jump in range(1, last_jump):  # 이전 점프보다 작은 거리만큼만 점프
        if pos - jump >= 0:  # 음수 위치로는 점프할 수 없음
            ways += find_ways(pos - jump, k - 1, jump)
            ways %= MOD

    memo[(pos, k, last_jump)] = ways
    return ways

def solution(n, k):
    total_ways = 0
    for first_jump in range(1, n + 1):
        total_ways += find_ways(n - first_jump, k - 1, first_jump)
        total_ways %= MOD

    return total_ways

# Test
print(solution(9, 3))  # 3
print(solution(10, 2))  # 4
print(solution(9, 4))  # 0
