#반복문을 통한 메모이제이션 피보나치 구현

d= [0]*100

d[1]=1
d[2]=1
n=6
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]

print(d[n])
