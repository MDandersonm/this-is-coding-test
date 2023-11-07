# 현재 잔액 n과 거래 횟수 m을 입력받음
n, m = map(int, input().split())

# 예약결제 대기 목록
reservation_queue = []

for _ in range(m):
    # 거래 내역을 입력받음
    transaction, amount = input().split()
    amount = int(amount)

    # deposit일 경우
    if transaction == "deposit":
        n += amount

        # 예약결제 대기 목록 처리
        while reservation_queue and n >= reservation_queue[0]:
            n -= reservation_queue.pop(0)

    # pay일 경우
    elif transaction == "pay":
        if n >= amount:
            n -= amount

    # reservation일 경우
    elif transaction == "reservation":
        if not reservation_queue and n >= amount:
            n -= amount
        else:
            reservation_queue.append(amount)

print(n)  # 잔액 출력
