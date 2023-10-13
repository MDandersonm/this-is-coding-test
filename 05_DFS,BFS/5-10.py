#음료수 얼려먹기 - 0 으로 연결되어있는 영역개수
n,m = map(int,input().split()) # 4행 5열
graph=[]
# for _ in range(n):
#     row = input()
#     row_list = [int(char) for char in row]
#     graph.append(row_list)
# print(graph)
# #graph,시작점,
# count=0
#
# def dfs(graph, x, y):  # x:행번호 y:열번호
#     if graph[x][y] == 0:
#         list1 = []
#         graph[x][y] = 1
#         if (x + 1) <= (n - 1) and graph[x + 1][y] != 1:  # 3<=3
#             list1.append((x + 1, y))  # 남
#         if x - 1 >= 0 and graph[x - 1][y] != 1:
#             list1.append((x - 1, y))  # 북
#         if (y + 1) <= (m - 1) and graph[x][y + 1] != 1:  # <=4 열번호
#             list1.append((x, y + 1))  # 동
#         if y - 1 >= 0 and graph[x][y - 1] != 1:
#             list1.append((x, y - 1))  # 서
#         print(list1)
#         for (x, y) in list1:
#             if graph[x][y] != 1:
#                 dfs(graph, x, y)
#
#
# for x in range(n):
#     for y in range(m):
#         if graph[x][y] == 0:
#             dfs(graph,x,y)
#             print("카운트업")
#             count += 1
#
# print(count)


#answer
for _ in range(n):
    graph.append(list(map(int,input())))
print(graph)
result=0
def dfs(x,y): #x행번호 y열번호
    if x<0 or y<0 or x>=n or y>=m :
        return False #범위를 넘어서면 false
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x - 1,y)
        dfs(x + 1, y)
        dfs(x , y-1)
        dfs(x , y+1)
        return True
    return False #이미 지나왔거나 1로 막혀있으면 false

for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result+=1

print(result)