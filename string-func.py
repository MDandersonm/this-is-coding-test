#숫자로 구성된 문자열의 각 자리 수의 합
def sum_of_digits(number_str):
    return sum(int(digit) for digit in number_str)
