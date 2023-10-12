#시각 - 3이 포함된 시각의 모든 경우의 수
n= int(input()) #n=5

h=0
m=0 #03분 13,23,, 30~39분,43,53, #15번
s=0 #3초 30~39초 =>11번

cnt=0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if str(h).find('3') >=0 or str(m).find('3') >=0  or str(s).find('3') >=0 :
                cnt+=1
print(cnt)
