#곱하기 혹은 더하기 -  각 자리수가 0또는1이면 더하기 아니면 곱하기
s=input()
#
# if s[0] in ['0','1']:
#     result=0
# else :
#     result =1
#
# flg=False #전값이 0또는 1이었다는 표시
# for str in s:
#     if str in ['0','1']:
#         result += int(str)
#         flg=True
#     else:
#         if flg==True:
#             result += int(str)
#             flg=False
#         else:
#             result *= int(str)
#
# print(result)

#answer

result= int(s[0])  #첫숫자를 시작점으로 잡아주면되는구나.

for i in range(1,len(s)):
    if (result in [0,1]) or (int(s[i]) in[0,1]):
        result +=int(s[i])
    else:
        result *=int(s[i])
print(result)