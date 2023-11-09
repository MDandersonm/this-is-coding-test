#시간초과

def count_loss_cases(n, m, k, turn=0):
    # Base Cases
    # n 또는 m이 0이면 경우의 수 1을 반환
    if n == 0 or m == 0:
        return 1
    # k번 진행 후 아무도 구슬을 잃지 않았다면 경우의 수 0을 반환
    if turn == k:
        return 0

    # 구름이가 이기는 경우 (상대방의 구슬 1개 감소 ,내꺼 하나증가)
    case1 = count_loss_cases(n+1, m - 1, k, turn + 1)
    # 구름이가 지는 경우 (구름이의 구슬 1개 감소, 내꺼 하나 감소)
    case2 = count_loss_cases(n - 1, m+1, k, turn + 1)
    # 무승부의 경우 (아무 변화 없음)
    case3 = count_loss_cases(n, m, k, turn + 1)
    return case1 + case2 + case3

# 입력값을 받음
n, m, k = map(int, input().split())

# 결과 출력
print(count_loss_cases(n, m, k))
