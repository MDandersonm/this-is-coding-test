#왕실의 나이트 - 8x8체스판의 특정 지점에서 이동할수있는 경우의수
data=input()
# x=ord(data[0])-96 #a가 1 h가8
# y=int(data[1])
#
# dx=[2,2,-2,-2,1,-1,1,-1]
# dy=[1,-1,1,-1,2,2,-2,-2]
#
# cnt=0
# for i in range(8):
#     nx = x+dx[i]
#     ny=  y+dy[i]
#     if nx<1 or ny<1 or nx>8 or ny>8:
#         continue
#     cnt+=1
#
# print(cnt)

#answer
cnt=0
x=ord(data[0])-ord('a')+1
y=int(data[1])
print(x,y)
steps=[(-2,-1),(-2,+1),(2,-1),(2,1),(1,2),(1,-2),(-1,2),(-1,-2)]

for s in steps:
    dx=x+s[0]
    dy=y+s[1]
    if dx>=1 and dx<=8 and dy>=1 and dy<=8:
        cnt+=1
print(cnt)