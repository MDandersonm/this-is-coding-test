n = int(input())

# 각 가구마다 물이 나가는 횟수와 들어오는 횟수를 기록하기 위한 두 개의 리스트 초기화
out_flow = [0] * (n+1)
in_flow = [0] * (n+1)

for _ in range(n-1):
    s, e = map(int, input().split())
    out_flow[s] += 1
    in_flow[e] += 1

# 물탱크를 설치해야 하는 위치는 물이 나가지만 들어오지 않는 가구
for i in range(1, n+1):
    if out_flow[i] > 0 and in_flow[i] == 0:
        print(i)
        break
