#모험가 길드  공포도가x인 모험가는 반드시 x명이상으로 구성한 모험가 그룹에 참가. 최대 몇개의 모험가 그룹을 만들수있는가
n=int(input()) #5
array=list(map(int,input().split())) #2 3 1 2 2

#answer
array.sort() #[1 2 2 2 3]
group=0
count=0
for i in array:
    count += 1
    if count>=i:
        group += 1
        count =0
print(group)