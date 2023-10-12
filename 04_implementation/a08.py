#문자열 재정렬- 알파벳과 숫자 분리
str1= input()

alpha=[]
number=0
for s in str1:
    if s.isalpha():
        alpha.append(s)
    else:
        number+= int(s)
alpha.sort()

first="".join(alpha)
second=str(number)
print(first+second)
