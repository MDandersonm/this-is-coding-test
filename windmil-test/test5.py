# 케이크 조각의 개수 n과 k를 입력 받는다
n, k = map(int, input().split())

# 남아있는 케이크 조각을 저장할 리스트 초기화
cake_pieces = list(range(1, n + 1))

# 현재 먹을 조각의 인덱스 초기화 (1번 조각부터 시작)
current_index = 0

while len(cake_pieces) > 2:
    # 현재 조각 먹기
    del cake_pieces[current_index]

    # k번째 조각으로 이동 (하지만 이미 조각을 먹었기 때문에 k-1을 더해준다)
    current_index = (current_index + k - 1) % len(cake_pieces)

# 남은 케이크 조각 출력
print(cake_pieces[0], cake_pieces[1])
