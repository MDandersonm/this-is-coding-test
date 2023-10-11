#N이 1이 될때까지 최소 횟수 구하기  1씩빼든지, K로 나누기
n,k= map(int, input().split()) # 25 5

#mysol

# cnt=0
# while True:
#     if n==1: break
#     if n%k==0:
#         n= n//k
#     else:
#         n=n-1
#     cnt+=1
# print(cnt)


#my_answer  n=25 k=3
# result=0
# while True:
#     result += n%k #25%3 =1    ,  8%3 =2   , 2%3=2
#     n= n -n%k  #25-1=24,   8-2=6
#     if n<k: #24<k  6<3
#         break
#     result +=1
#     n= n//k #24//3 =8,    6//3= 2
#
# print(result-1)


#answer n=25 k=3
result=0
while True:
    target= (n//k )*k #24  , 6   ,0
    result += n-target #25-24 =1  , 8-6=2 ,2-0=2
    n=target
    if n<k: break;
    n= n//k # 24//3=8 ,    2//3=2
    result+=1

result += (n-1)
print(result)



