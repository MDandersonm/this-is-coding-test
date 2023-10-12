#럭키 스트레이트  -문자열숫자의 각 자리수의 합
n=input()
l=len(n) #6

left=n[:(l//2)] # 0,1,2
right=n[l//2:] #3,4,5

def word_sum(str):
    return sum(list(map(int, list(str))))
print("LUCKY") if word_sum(left)==word_sum(right) else print("READY")


#answer1
def sum_of_digits(number_str):
    return sum(int(digit) for digit in number_str)

