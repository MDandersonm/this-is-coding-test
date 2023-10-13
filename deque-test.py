from collections import deque
data = deque([2,3,4])
data.appendleft(1)
data.append(5) #추가
print(data)
data.pop() 
print(data)
data.popleft() #선입선출삭제
print(data)
print(list(data))