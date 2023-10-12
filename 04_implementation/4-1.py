#상하좌우 - (1,1)에서 상하좌우 이동
n= int(input()) #5 x 5
# data = list(input().split())
#
# start=[1,1] #행, 열
# for x in data:
#     if x=='L':
#         if start[1] !=1:
#             start[1]-=1
#     elif x=='R':
#         if start[1] != n:
#             start[1]+=1
#
#     elif x == 'D':
#         if start[0] != n:
#             start[0] += 1
#     elif x == 'U':
#         if start[0] != 1:
#             start[0] -= 1
#
# print(start[0],start[1])

#answer
data= input().split()
print(data)
x,y=1,1 #행 열
move_types=['L','R','U','D']
dx=[0,0,-1,1]
dy=[-1,1,0,0]

for alpha in data:
    for i in range(len(move_types)):
        if alpha==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or ny>n or nx>n:
        continue
    x=nx
    y=ny
print(x,y)