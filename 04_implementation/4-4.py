#게임 개발- 한칸씩 움직이는 경우의수
# n,m= map(int,input().split())
# x,y,d=  map(int,input().split()) #start지점 1,1
#
# list1=[]
# for _ in range(m):
#     list1.append(list(map(int,input().split())))
# print(list1)
#
# if d==1:
#     d=3
# elif d==3:
#     d=1
#
# dx=[-1,0,+1,0] #북 서 남 동  #행
# dy=[0,-1,0,1] #열
# cnt=1
# flg=0
# while True:
#     d += 1 #왼쪽으로 회전
#
#     nx=x+dx[(d)%4]
#     ny=y+dy[(d)%4]
#     print(nx,ny,"direction:",(d)%4)
#     print("list1[nx][ny]",list1[nx][ny],"flg:",flg)
#     if list1[nx][ny] !=0:
#         print("nx:", nx, "ny:", ny,"list1[nx][ny]",list1[nx][ny])
#         flg+=1
#         if flg == 4:
#             nx = x - dx[(d) % 4]
#             ny = y - dy[(d) % 4]
#             print("nx:", nx, "ny:", ny)
#             if list1[nx][ny] == 2:
#                 list1[x][y] = 2 #되돌아 갈때도 2로표기
#                 x, y = nx, ny
#             elif list1[nx][ny] == 1:
#                 print("종료")
#                 break
#             flg = 0
#         continue
#     list1[x][y]=2 #지나온곳은 2로표기
#     x,y=nx,ny
#     cnt+=1
#     flg=0
# print(cnt)

#answer

n,m= map(int,input().split())
x,y,direction=  map(int,input().split())
list1=[]
for _ in range(m):
    list1.append(list(map(int,input().split())))
print(list1)
#방문한 위치
d=[ [0]*m for _ in range(n)]
def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3
dx=[-1,0,1,0]#행
dy=[0,1,0,-1]#열
count=1
turn_time=0;
while True:
    turn_left()#좌로 회전
    nx=x+dx[direction]
    ny=y+dy[direction]
    if list1[nx][ny] ==0 and d[nx][ny]==0 :
        x,y=nx,ny
        count+=1
        d[x][y]=1
        turn_time = 0;
        continue
    turn_time+=1

    if(turn_time==4):
        nx = x - dx[direction]
        ny = y - dy[direction]
        if list1[nx][ny] ==1: break
        elif d[nx][ny]==1:
            x,y=nx,ny
        turn_time=0;
print(count)