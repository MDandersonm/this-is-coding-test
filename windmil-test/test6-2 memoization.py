def count_loss_cases(n, m, k, turn=0, memo=None):
    # 메모 객체 초기화
    if memo is None:
        memo = {}

    # 이미 계산된 값이 있는지 확인
    if (n, m, turn) in memo:
        return memo[(n, m, turn)]

    # Base Cases
    if n == 0 or m == 0:
        return 1
    if turn == k:
        return 0

    # 구름이가 이기는 경우 (상대방의 구슬 1개 감소, 내꺼 하나 증가)
    case1 = count_loss_cases(n+1, m - 1, k, turn + 1, memo)
    # 구름이가 지는 경우 (구름이의 구슬 1개 감소, 상대방의 구슬 1개 증가)
    case2 = count_loss_cases(n - 1, m+1, k, turn + 1, memo)
    # 무승부의 경우 (아무 변화 없음)
    case3 = count_loss_cases(n, m, k, turn + 1, memo)

    # 계산한 값을 저장
    memo[(n, m, turn)] = case1 + case2 + case3
    print(memo)

    return memo[(n, m, turn)]

# 입력값을 받음
n, m, k = map(int, input().split())

# 결과 출력
print(count_loss_cases(n, m, k))
