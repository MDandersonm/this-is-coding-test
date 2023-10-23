#성적이 낮은 순서로 학생 출력하기

n=int(input())
list1=[]
for _ in range(n):
    x,y=input().split()
    list1.append((x,y))
print(list1)

def sort(list1):
    return list1[1]
list1.sort(key=sort)

for li in list1:
    print( li[0],end=' ')

#answer
array= sorted(list1,key=lambda x:x[1]) #이렇게 lambda를 사용할 수도 있다.
print(array)