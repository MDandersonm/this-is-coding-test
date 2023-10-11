#리스트컴프리헨션


array1 = [i for i in range(20) if i%2==1] # range(20) :0부터19까지
print(array1)
array2= [i*i for i in range(1,10)]  # range(1,10) : 1부터9까지
print(array2)

#리스트메서드
list1=[1,4,3]
#추가 저장
list1.append(5)
print(list1)
#정렬 저장
list1.sort()
print(list1)
#list1.sort(reverse=True)

#정렬 저장x
list2= sorted(list1, reverse=True)
print(list2)

#순서 뒤집어 저장
list2.reverse() 
print(list2)

#삽입 저장
list2.insert(3,99)
print(list2)

#특정 데이터 개수 출력
a=list2.count(99)
print(a)

#특정 데이터 삭제 저장
list2.remove(99)
print(list2)

#특정 리스트 요소 삭제
del list2[1]
print(list2)
#특정값의 index 출력
print(list2.index(4))

#pop 맨 마지막 값 뽑아내기
print("pop",list2.pop())
print(list2)
#pop 특정인덱스값 뽑아내기
print("pop",list2.pop(1))
print(list2)


#문자열 관련함수
a= "hobby"
print(a.count('b'))
print(a.find('b'))
print(a.find('z')) #없으면 -1 반환
print(a.index('y')) #없으면 오류

#문자열 삽입출력
a1= ",".join(a)
print(a)
print(a1)

#문자열 교체출력
a2=a1.replace('b','z')
print(a2)

#문자열나누기
a3=a2.split(',')
print(a3)

#딕셔너리
a=dict()
a['b']='banana'
a['a']='apple'
a['g']='grape'
print(a)
for key in a.keys():
    print(key)
for val in a.values():
    print(val)
for key,val in a.items():
    print(key,val)
print(a.get('b'))

print('b' in a)

#enumerate
for i,name in enumerate(['hell','foo','bar']):
    print(i,name)

#filter
f= list(filter(lambda x: x>0, [1,-3,2,-4,5]))
print(f)