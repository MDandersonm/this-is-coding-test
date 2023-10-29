#재귀
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:

        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
#메모이제이션
def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
        print(memo)
        return memo[n]
#반복문
def fibonacci_iterative(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

# r= fibonacci_recursive(6)
r= fibonacci_memoization(6);
print(r)