n, m = map(int, input().split())

pieces = [(4, 4), (4, 2), (2, 2), (1, 1)]

def can_place(board, piece, x, y):
    for i in range(piece[0]):
        for j in range(piece[1]):
            if x + i >= n or y + j >= m or board[x + i][y + j] == 1:
                #현재 검사하려는 칸 (x + i, y + j)가 보드의 경계를 벗어나지 않는지 확인합니다. 만약 벗어나면 조각을 해당 위치에 놓을 수 없으므로 False를 반환합니다.
                #(x + i, y + j) 위치에 이미 조각이 놓여 있는 경우 (즉, board[x + i][y + j]의 값이 1인 경우), 새로운 조각을 그 위치에 놓을 수 없으므로 False를 반환합니다.
                return False
    return True

def place(board, piece, x, y, val):
    for i in range(piece[0]):
        for j in range(piece[1]):
            board[x + i][y + j] = val
#board에 (x, y) 위치에서 시작하여 주어진 piece 크기의 조각을 놓거나 제거하는 기능을 합니다. 조각을 놓을 때는 val 값을 1로 설정하고, 조각을 제거할 때는 val 값을 0으로 설정하여 사용합니다.

def solve(board):
    x, y = -1, -1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0: #아무런 조각도 놓여있지않았으면
                x, y = i, j
                break
        if x != -1:
            break
    if x == -1:
        return 1#만약 첫 번째 빈 칸을 찾지 못했다면 (즉, x가 -1인 경우), 보드의 모든 칸이 채워진 것을 의미합니다. 이 경우, 현재의 조합이 유효하므로 1을 반환합니다.
    count = 0
    for piece in pieces:
        if can_place(board, piece, x, y):
            place(board, piece, x, y, 1)
            count += solve(board)
            place(board, piece, x, y, 0)# place 함수를 다시 사용하여 방금 놓았던 조각을 보드에서 제거합니다. 이로써 원래의 상태로 돌아와 다음 조각에 대한 시도를 준비합니다.
    return count

board = [[0] * m for _ in range(n)]
# board는 2차원 리스트로, 주어진 보드의 상태를 나타냅니다. 각 요소는 보드의 특정 위치에 대한 정보를 가지고 있으며, 주로 아래 두 가지 값을 가집니다:
#
# 0: 해당 위치에 아무런 조각도 놓이지 않았음을 나타냅니다. 즉, 빈 칸을 의미합니다.
# 1: 해당 위치에 조각이 놓였음을 나타냅니다.
# 예를 들어, board[2][3] = 0이면 (2, 3) 위치에는 조각이 놓이지 않았다는 것을 의미하고, board[2][3] = 1이면 (2, 3) 위치에 조각이 놓여 있다는 것을 의미합니다.
print(solve(board))

# x와 y는 보드 상에서의 좌표를 나타내는 변수들입니다.
#
# x: 보드의 행 번호를 나타냅니다.
# y: 보드의 열 번호를 나타냅니다.
# 즉, board[x][y]는 보드 상에서 (x, y) 위치에 있는 칸의 값을 나타냅니다.
#
# 코드에서 x와 y는 첫 번째로 발견되는 빈 칸(즉, 값이 0인 칸)의 위치를 찾아 저장하는 데 사용됩니다. 처음에는 -1로 초기화됩니다. 이는 아직 빈 칸을 찾지 못했다는 것을 나타냅니다.
#
# 코드를 실행하는 중에 만약 board[i][j] == 0인 칸을 발견한다면, x와 y는 각각 i와 j 값으로 갱신됩니다. 이는 첫 번째로 발견된 빈 칸의 위치를 나타냅니다.
#
# 따라서 x와 y의 값이 -1이 아니라면, 그것은 첫 번째 빈 칸의 위치가 (x, y)임을 의미합니다.
