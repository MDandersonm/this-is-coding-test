#문자열 압축 - 중복문자 숫자로 압축    20 카카오 신입공채

# def solution(s):
#     s+=" "
#     result=""
#     temp=s[0]
#     count=1
#     for i in range(1,len(s)):
#         if temp==s[i]:
#             count+=1
#         else:
#             if count !=1:
#                 result+= str(count)+temp
#             else:
#                 result += temp
#             temp=s[i]
#             count=1
#     return result

# def solution(s):
#     k=2
#     s+=" "
#     result=""
#     temp=s[:k]#0부터1까지 2글자
#     count=1
#     for i in range(k,len(s),k): # i=2부터 , 2개씩점프
#         if temp==s[i:i+k]:
#             count+=1
#         else:
#             if count !=1:
#                 result+= str(count)+temp
#             else:
#                 result += temp
#             temp=s[i:i+k]
#             count=1
#     return result


def solution(s):
    answer=[]
    for k in range(1,(len(s)//2)+1):
        s += " "
        result=""
        temp=s[:k]#0부터1까지 2글자
        count=1
        for i in range(k,len(s),k): # i=2부터 , 2개씩점프
            #print("i",i,"k",k,"len(s)",len(s))
            if temp==s[i:i+k]:
                count+=1
            else:
                if count !=1:
                    result+= str(count)+temp.strip()
                else:
                    #print("temp.strip()",temp.strip())
                    result += temp.strip()
                temp=s[i:i+k]
                count=1
        # print("result",result)
        answer.append(len(result))
    return min(answer) if len(answer) !=0 else 1

# r=solution("aabbaccc")
# r=solution("ababcdcdababcdcd") #2ab2cd2ab2cd
# r=solution('abcabcdede')
# r=solution('abcabcabcabcdededededede')
r=solution('xababcdcdababcdcd')
#r=solution('a')
print(r)


#answer

