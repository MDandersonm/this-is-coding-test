#문자열 뒤집기 - 연속된수가 끊기는 지점 횟수찾기
str=input()
#
# zero=0
# one=0
# now=str[0] # '0'
#
# if str[-1]=='0':
#     zero+=1
# else:
#     one+=1
#
# for s in str:
#     if s=='0' and s==now:
#         continue
#     elif s=='0' and s!=now:
#         one+=1
#         now = '0'
#     elif s=='1' and s==now:
#         continue
#     elif s=='1' and s!=now:
#         zero+=1
#         now='1'
#
# print(  min(zero,one))

#answer
count0=0 #전부 0으로바뀌는 경우
count1=0 #전부 1로 바뀌는 경우

if str[0]=='1':
    count0 +=1
else:#첫문자가 0이면
    count1 +=1

#두번째원소부터 모든 원소를 확인

for i in range(len(str)-1):
    if str[i] != str[i+1] :
        if str[i+1]=='1': # 01
            count0+=1
        else: #10일때
            count1+=1
print( min(count0, count1))