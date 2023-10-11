#큰 수의 법칙
n,m,k=map(int,input().split()) # 5 8 3
array=list(map(int,input().split()))
print(n,m,k)
print(array)

#my sol
ans=0
cnt=1

sorted_array= sorted(array)
for i in range(m): #m = 0부터 7까지
    if cnt <= k: #cnt = 1,2,3  k=3
        ans += sorted_array[-1]
    else:
        ans += sorted_array[-2]
        cnt=0
    cnt +=1

print(ans)

#answer
array.sort()

first= array[-1]
second= array[-2]

count= (m//(k+1))*k + m%(k+1) # 최대값이 나오는 횟수

ans2 = count * first
ans2 += (m-count) * second
print(ans2)


