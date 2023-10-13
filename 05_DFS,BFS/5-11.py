#미로탈출 - 최단경로 거리수

n,m = map(int,input().split()) #행 열
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

print(graph)

# cnt=0
# def dfs(x,y):
#     global cnt
#     if x>n or x<1 or y>m or y<1:
#         return False
#     if x==n and y==m :
#         return cnt
#
#     cnt += 1
#     if graph[x,y] ==1:
#         dfs(x-1,y)
#         dfs(x + 1, y)
#         dfs(x , y-1)
#         dfs(x , y+1)
#
#         return True
#     return False
#
# r=dfs(1,1)
# print(r)




from collections import deque

# def bfs():
#     queue = deque()
#     queue.append([0, 0,1])
#     graph[0][0] = 0
#     result=[]
#     while queue:
#         print("queue",queue)
#         node = queue.popleft()
#         print("node",node)
#         if node[0]==n-1 and node[1]==m-1:
#             result.append(node[2])
#         list1=[]
#         if node[0]+1>=0 and node[0]+1<=n-1 and graph[node[0]+1][node[1]]==1 :
#             list1.append([node[0]+1, node[1],node[2]+1])
#         if node[0] - 1 >= 0 and node[0] - 1 <= n-1 and graph[node[0]-1][node[1]]==1:
#             list1.append([node[0] - 1, node[1],node[2]+1])
#         if node[1]+1 >= 0 and node[1]+1 <= m-1 and graph[node[0]][node[1]+1]==1:
#             list1.append([node[0] , node[1]+1,node[2]+1])
#         if node[1]-1 >= 0 and node[1]-1 <= m-1 and graph[node[0]][node[1]-1]==1:
#             list1.append([node[0] , node[1]-1,node[2]+1])
#         for li in list1:
#             if graph[li[0]][li[1]] ==1:
#                 queue.append(li)
#                 graph[li[0]][li[1]] = 0
#     print(result)
#     return min(result)
#
#
# r=bfs()
# print(r)

#answer
dx=[1,-1,0,0] #동 서 남 북
dy=[0,0,-1,1]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if nx>=n or nx<0 or ny >=m or ny<0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

r=bfs(0,0)
print(r)

